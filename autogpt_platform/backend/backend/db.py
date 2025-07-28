from backend.app import run_processes
from backend.executor import DatabaseManager

def main():
    """
    roda todos os processos necessários para a api rest do servidor do autogpt.
    """
    run_processes(DatabaseManager())

if __name__ == "__main__":
    main()