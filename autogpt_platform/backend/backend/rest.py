from backend.app import run_processes
from backend.executor import DatabaseManager
from backend.notifications.notifications import NotificationManager
from backend.server.rest_api import AgentServer

def main():
    """
    executa todos os processos necessários para a api rest do servidor autogpt.
    """

    run_processes(
        NotificationManager(),
        DatabaseManager(),
        AgentServer()
    )

if __name__ == "__main__":
    main()