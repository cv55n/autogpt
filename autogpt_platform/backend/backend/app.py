import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.util.process import AppProcess

logger = logging.getLogger(__name__)

def run_processes(*processes: "AppProcess", **kwargs):
    """
    executa todos os processos no aplicativo. o último processo é executado em primeiro plano.
    inclui tratamento de erros aprimorado e gerenciamento do ciclo de vida do processo.
    """

    try:
        # executa todos os processos, exceto o último, em segundo plano
        for process in processes[:-1]:
            process.start(background=True, **kwargs)

        # executa o último processo em primeiro plano
        processes[-1].start(background=False, **kwargs)
    finally:
        for process in processes:
            try:
                process.stop()
            except Exception as e:
                logger.exception(f"[{process.service_name}] não conseguiu ser parado: {e}")

def main(**kwargs):
    """
    executa todos os processos necessários para o servidor autogpt (apis rest e websocket).
    """

    from backend.executor import DatabaseManager, ExecutionManager, Scheduler
    from backend.notifications import NotificationManager
    from backend.server.rest_api import AgentServer
    from backend.server.ws_api import WebsocketServer

    run_processes(
        DatabaseManager(),
        ExecutionManager(),
        Scheduler(),
        NotificationManager(),
        WebsocketServer(),
        AgentServer(),

        **kwargs
    )

if __name__ == "__main__":
    main()