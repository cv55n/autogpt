import inspect
import logging
import secrets
from typing import Any, Callable, Optional

from fastapi import HTTPException, Request, Security
from fastapi.security import APIKeyHeader, HTTPBearer
from starlette.status import HTTP_401_UNAUTHORIZED

from .config import settings
from .jwt_utils import parse_jwt_token

security = HTTPBearer()

logger = logging.getLogger(__name__)

async def auth_middleware(request: Request):
    if not settings.ENABLE_AUTH:
        # se a autenticação estiver desabilitada, permita que a solicitação prossiga
        logger.warning("autenticação desabilitada")

        return {}
    
    security = HTTPBearer()

    credentials = await security(request)

    if not credentials:
        raise HTTPException(status_code=401, detail="header de autorização ausente")

    try:
        payload = parse_jwt_token(credentials.credentials)
        request.state.user = payload

        logger.debug("token decodificado com sucesso")
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
    return payload

class APIKeyValidator:
    """
    validador de chave de api configurável que suporta funções de validação
    personalizadas para aplicativos fastapi.

    essa classe oferece uma maneira flexível de implementar autenticação de
    chave de api com lógica de validação personalizada opcional. pode ser
    usada para correspondência simples de tokens ou cenários de validação
    mais complexos, como consultas em bancos de dados.

    exemplos:
        validação de token simples:
        ```python
        validator = APIKeyValidator(
            header_name="X-API-Key",
            expected_token="your-secret-token"
        )

        @app.get("/protected", dependencies=[Depends(validator.get_dependency())])
        def protected_endpoint():
            return {"message": "acesso garantido"}
        ```

        validação personalizada com consulta de banco de dados:
        ```python
        async def validate_with_db(api_key: str):
            api_key_obj = await db.get_api_key(api_key)

            return api_key_obj if api_key_obj and api_key_obj.is_active else None

        validator = APIKeyValidator(
            header_name="X-API-Key",
            validate_fn=validate_with_db
        )
        ```

    args:
        header_name (str): o nome do header que contém a chave de api
        expected_token (Optional[str]): o valor esperado da chave de api para correspondência de token simples
        validate_fn (Optional[Callable]): função de validação personalizada que recebe uma string de chave de
            api e retorna um booleano ou objeto. pode ser assíncrona
        error_status (int): código de status http a ser usado para erros de validação
        error_message (str): mensagem de erro a ser retornada quando a validação falha
    """

    def __init__(
        self,
        header_name: str,
        expected_token: Optional[str] = None,
        validate_fn: Optional[Callable[[str], bool]] = None,
        error_status: int = HTTP_401_UNAUTHORIZED,
        error_message: str = "chave de api inválida"
    ):
        # cria o apikeyheader como uma propriedade de classe
        self.security_scheme = APIKeyHeader(name=header_name)
        self.expected_token = expected_token
        self.custom_validate_fn = validate_fn
        self.error_status = error_status
        self.error_message = error_message

    async def default_validator(self, api_key: str) -> bool:
        if not self.expected_token:
            raise ValueError(
                "token esperado necessário para ser definido ao usar a validação padrão do validador de chave de api"
            )
        
        return secrets.compare_digest(api_key, self.expected_token)
    
    async def __call__(
        self, request: Request, api_key: str = Security(APIKeyHeader)
    ) -> Any:
        if api_key is None:
            raise HTTPException(status_code=self.error_status, detail="chave de api ausente")

        # utiliza a validação personalizada se fornecida, caso contrário, use verificação de igualdade padrão
        validator = self.custom_validate_fn or self.default_validator

        result = (
            await validator(api_key)
            if inspect.iscoroutinefunction(validator)
            else validator(api_key)
        )

        if not result:
            raise HTTPException(
                status_code=self.error_status, detail=self.error_message
            )

        # armazena o resultado da validação no estado da solicitação se não for apenas um boolean
        if result is not True:
            request.state.api_key = result

        return result
    
    def get_dependency(self):
        """
        retorna uma dependência chamável que o fastapi reconhecerá como um esquema de segurança
        """

        async def validate_api_key(
            request: Request, api_key: str = Security(self.security_scheme)
        ) -> Any:
            return await self(request, api_key)

        # isso ajuda o fastapi a reconhecê-lo como uma dependência de segurança
        validate_api_key.__name__ = f"validate_{self.security_scheme.model.name}"
        
        return validate_api_key