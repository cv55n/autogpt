from backend.app import run_processes
from backend.server.ws_api import WebsocketServer

def main():
    """
    executa todos os processos necessários para a api websocket do servidor autogpt.
    """

    run_processes(WebsocketServer())

if __name__ == "__main__":
    main()