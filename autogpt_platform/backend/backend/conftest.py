import logging
import os

import pytest
from dotenv import load_dotenv

from backend.util.logging import configure_logging

os.environ["ENABLE_AUTH"] = "false"

load_dotenv()

# nota: você pode rodar os testes como o --log-cli-level=info para ver os logs

# configurando o logging
configure_logging()

logger = logging.getLogger(__name__)

# reduz o log do prisma a não ser que prisma_debug esteja configurado
if not os.getenv("PRISMA_DEBUG"):
    prisma_logger = logging.getLogger("prisma")
    prisma_logger.setLevel(logging.INFO)

@pytest.fixture(scope="session")
async def server():
    from backend.util.test import SpinTestServer

    async with SpinTestServer() as server:
        yield server

@pytest.fixture(scope="session", autouse=True)
async def graph_cleanup(server):
    created_graph_ids = []
    original_create_graph = server.agent_server.test_create_graph

    async def create_graph_wrapper(*args, **kwargs):
        created_graph = await original_create_graph(*args, **kwargs)

        # extrai o user_id corretamente
        user_id = kwargs.get("user_id", args[2] if len(args) > 2 else None)
        created_graph_ids.append((created_graph.id, user_id))

        return created_graph
    
    try:
        server.agent_server.test_create_graph = create_graph_wrapper

        yield # isso roda a função de teste
    finally:
        server.agent_server.test_create_graph = original_create_graph

        # deleta os gráficos criados
        for graph_id, user_id in created_graph_ids:
            if user_id:
                resp = await server.agent_server.test_delete_graph(graph_id, user_id)

                num_deleted = resp["version_counts"]

                assert num_deleted > 0, f"gráfico {graph_id} não foi deletado."