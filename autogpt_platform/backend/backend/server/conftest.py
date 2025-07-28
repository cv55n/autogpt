"""dispositivos de teste comuns para testes de servidor."""

import pytest
from pytest_snapshot.plugin import Snapshot

@pytest.fixture
def configured_snapshot(snapshot: Snapshot) -> Snapshot:
    """dispositivo de captura instantânea pré-configurado com configurações padrão."""
    snapshot.snapshot_dir = "snapshots"

    return snapshot

# constantes de id de teste
TEST_USER_ID = "test-user-id"
ADMIN_USER_ID = "admin-user-id"
TARGET_USER_ID = "target-user-id"