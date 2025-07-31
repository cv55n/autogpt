import hashlib
import secrets
from typing import NamedTuple

class APIKeyContainer(NamedTuple):
    """contêiner para as partes da chave de api."""

    raw: str
    prefix: str
    postfix: str
    hash: str

class APIKeyManager:
    PREFIX: str = "agpt_"

    PREFIX_LENGTH: int = 8
    POSTFIX_LENGTH: int = 8

    def generate_api_key(self) -> APIKeyContainer:
        """gere uma nova chave de api com todas as suas partes."""

        raw_key = f"{self.PREFIX}{secrets.token_urlsafe(32)}"

        return APIKeyContainer(
            raw=raw_key,
            prefix=raw_key[: self.PREFIX_LENGTH],
            postfix=raw_key[-self.POSTFIX_LENGTH :],
            hash=hashlib.sha256(raw_key.encode()).hexdigest()
        )
    
    def verify_api_key(self, provided_key: str, stored_hash: str) -> bool:
        """verifica se uma chave de api fornecida corresponde ao hash armazenado."""

        if not provided_key.startswith(self.PREFIX):
            return False
        
        provided_hash = hashlib.sha256(provided_key.encode()).hexdigest()

        return secrets.compare_digest(provided_hash, stored_hash)