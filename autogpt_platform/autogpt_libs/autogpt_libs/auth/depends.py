import fastapi

from .config import settings
from .middleware import auth_middleware
from .models import DEFAULT_USER_ID, User

def requires_user(payload: dict = fastapi.Depends(auth_middleware)) -> User:
    return verify_user(payload, admin_only=False)

def requires_admin_user(payload: dict = fastapi.Depends(auth_middleware)) -> User:
    return verify_user(payload, admin_only=True)

def verify_user(payload: dict | None, admin_only: bool) -> User:
    if not payload:
        if settings.ENABLE_AUTH:
            raise fastapi.HTTPException(
                status_code=401, detail="header de autorização ausente"
            )
        
        # isso lida com o caso quando a autenticação está desabilitada
        payload = {"sub": DEFAULT_USER_ID, "role": "admin"}

    user_id = payload.get("sub")

    if not user_id:
        raise fastapi.HTTPException(
            status_code=401, detail="id do usuário não encontrado no token"
        )
    
    if admin_only and payload["role"] != "admin":
        raise fastapi.HTTPException(status_code=403, detail="acesso de administração necessário")
    
    return User.from_payload(payload)

def get_user_id(payload: dict = fastapi.Depends(auth_middleware)) -> str:
    user_id = payload.get("sub")

    if not user_id:
        raise fastapi.HTTPException(
            status_code=401, detail="id do usuário não encontrado no token"
        )
    
    return user_id