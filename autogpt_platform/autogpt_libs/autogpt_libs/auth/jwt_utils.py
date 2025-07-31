from typing import Any, Dict

import jwt

from .config import settings

def parse_jwt_token(token: str) -> Dict[str, Any]:
    """
    analisa e valida um token jwt.

    :param token: o token a ser analisado
    :return: a carga útil decodificada
    :raises valueerror: se o token for inválido ou expirado
    """

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
            audience="authenticated"
        )

        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("token foi expirado")
    except jwt.InvalidTokenError as e:
        raise ValueError(f"token inválido: {str(e)}")