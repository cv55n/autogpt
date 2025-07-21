"""
este é um arquivo mínimo que deve ser executado pelos usuários para ajudá-los a gerenciar os projetos autogpt.

se você quiser contribuir, use apenas bibliotecas que fazem parte do python.
para garantir a eficiência, adicione as importações às funções para que somente o necessário seja importado.
"""

try:
    import click
except ImportError:
    import os

    os.system("pip3 install click")

    import click

@click.group()
def cli():
    pass

@cli.command()
def setup():
    """instala as dependências necessárias para o seu sistema. funciona com linux, macos e windows wsl."""

    import os
    import subprocess

    click.echo(
        click.style(
            """
       d8888          888             .d8888b.  8888888b. 88888888888 
      d88888          888            d88P  Y88b 888   Y88b    888     
     d88P888          888            888    888 888    888    888     
    d88P 888 888  888 888888 .d88b.  888        888   d88P    888     
   d88P  888 888  888 888   d88""88b 888  88888 8888888P"     888     
  d88P   888 888  888 888   888  888 888    888 888           888     
 d8888888888 Y88b 888 Y88b. Y88..88P Y88b  d88P 888           888     
d88P     888  "Y88888  "Y888 "Y88P"   "Y8888P88 888           888     
                                                                                                                                       
""",
            
            fg="green"
        )
    )

    script_dir = os.path.dirname(os.path.realpath(__file__))
    setup_script = os.path.join(script_dir, "setup.sh")

    install_error = False

    if os.path.exists(setup_script):
        click.echo(click.style("🚀 setup inicializado...\n", fg="green"))

        try:
            subprocess.check_call([setup_script], cwd=script_dir)
        except subprocess.CalledProcessError:
            click.echo(
                click.style("❌ ocorreu um erro durante a instalação.", fg="red")
            )

            install_error = True
    else:
        click.echo(
            click.style(
                "❌ erro: setup.sh não existe no diretório atual.", fg="red"
            )
        )

        install_error = True

    if install_error:
        click.echo(
            click.style(
                "\n\n🔴 se você precisa de ajuda, por favor crie um ticket no github em https://github.com/cv55n/autogpt/issues\n\n",

                fg="magenta",
                bold=True
            )
        )
    else:
        click.echo(click.style("🎉 configuração completa.\n", fg="green"))

@cli.group()
def agent():
    """comandos para criar, iniciar e parar agentes"""

    pass

@agent.command()
@click.argument("agent_name")
def create(agent_name: str):
    """cria um novo agente com o nome de agente fornecido"""

    import os
    import re
    import shutil

    if not re.match(r"\w*$", agent_name):
        click.echo(
            click.style(
                f"😞 nome de agente '{agent_name}' não é válido. ele deve não conter espaços ou caracteres especiais altém de -_",

                fg="red"
            )
        )

        return
    
    try:
        new_agent_dir = f"./agents/{agent_name}"
        new_agent_name = f"{agent_name.lower()}.json"

        if not os.path.exists(new_agent_dir):
            shutil.copytree("./forge", new_agent_dir)

            click.echo(
                click.style(
                    f"🎉 novo agente '{agent_name}' criado. o código para o seu novo agente está em: agents/{agent_name}",

                    fg="green"
                )
            )
        else:
            click.echo(
                click.style(
                    f"😞 agente '{agent_name}' já existe. insira um nome diferente para o seu agente, o nome precisa ser único",

                    fg="red"
                )
            )
    except Exception as e:
        click.echo(click.style(f"😢 ocorreu um erro: {e}", fg="red"))

@agent.command()
@click.argument("agent_name")
@click.option(
    "--no-setup",

    is_flag=True,
    help="desativa a execução do script de configuração antes de iniciar o agente"
)
def start(agent_name: str, no_setup: bool):
    """inicia o comando do agente"""

    import os
    import subprocess

    script_dir = os.path.dirname(os.path.realpath(__file__))

    agent_dir = os.path.join(
        script_dir,
        f"agents/{agent_name}"

        if agent_name not in ["original_autogpt", "forge"]
        else agent_name
    )

    run_command = os.path.join(agent_dir, "run")
    run_bench_command = os.path.join(agent_dir, "run_benchmark")

    if (
        os.path.exists(agent_dir) and os.path.isfile(run_command) and os.path.isfile(run_bench_command)
    ):
        os.chdir(agent_dir)

        if not no_setup:
            click.echo(f"⌛ rodando configuração para o agente '{agent_name}'...")

            setup_process = subprocess.Popen(["./setup"], cwd=agent_dir)
            setup_process.wait()

            click.echo()

        # fixme: não funciona: comando não encontrado: agbenchmark
        #
        # subprocess.Popen(["./run_benchmark", "serve"], cwd=agent_dir)
        #
        # click.echo("⌛ (re)iniciando o servidor do benchmark...")
        #
        # wait_until_conn_ready(8080)
        #
        # click.echo()

        subprocess.Popen(["./run"], cwd=agent_dir)

        click.echo(f"⌛ (re)iniciando o agente '{agent_name}'...")

        wait_until_conn_ready(8000)

        click.echo("✅ o aplicativo do agente foi iniciado e está disponível na porta 8000")
    elif not os.path.exists(agent_dir):
        click.echo(
            click.style(
                f"😞 agente '{agent_name}' não existe. por favor crie o agente primeiro.",

                fg="red"
            )
        )
    else:
        click.echo(
            click.style(
                f"😞 comando de rodar não existe no diretório do agente '{agent_name}'.",

                fg="red"
            )
        )

@agent.command()
def stop():
    """comando de parar o agente"""

    import os
    import signal
    import subprocess

    try:
        pids = subprocess.check_output(["lsof", "-t", "-i", ":8000"]).split()

        if isinstance(pids, int):
            os.kill(int(pids), signal.SIGTERM)
        else:
            for pid in pids:
                os.kill(int(pid), signal.SIGTERM)
    except subprocess.CalledProcessError:
        click.echo("nenhum processo rodando na porta 8000")

    try:
        pids = int(subprocess.check_output(["lsof", "-t", "-i", ":8000"]))

        if isinstance(pids, int):
            os.kill(int(pids), signal.SIGTERM)
        else:
            for pid in pids:
                os.kill(int(pid), signal.SIGTERM)
    except subprocess.CalledProcessError:
        click.echo("nenhum processo rodando na porta 8000")

@agent.command()
def list():
    """comando de listar os agentes"""

    import os

    try:
        agents_dir = "./agents"

        agents_list = [
            d

            for d in os.listdir(agents_dir)

            if os.path.isdir(os.path.join(agents_dir, d))
        ]

        if os.path.isdir("./original_autogpt"):
            agents_list.append("original_autogpt")
        if agents_list:
            click.echo(click.style("agentes disponíveis: 🤖", fg="green"))

            for agent in agents_list:
                click.echo(click.style(f"\t🐙 {agent}", fg="blue"))
        else:
            click.echo(click.style("nenhum agente encontrado 😞", fg="red"))
    except FileNotFoundError:
        click.echo(click.style("o diretório de agentes não existe 😢", fg="red"))
    except Exception as e:
        click.echo(click.style(f"ocorreu um erro: {e} 😢", fg="red"))

@cli.group()
def benchmark():
    """comandos para iniciar o benchmark e listar testes e categorias"""

    pass

@benchmark.command(context_settings=dict(ignore_unknown_options=True))
@click.argument("agent_name")
@click.argument("subprocess_args", nargs=-1, type=click.UNPROCESSED)
def start(agent_name, subprocess_args):
    """comando de iniciar o benchmark"""

    import os
    import subprocess

    script_dir = os.path.dirname(os.path.realpath(__file__))

    agent_dir = os.path.join(
        script_dir,

        f"agents/{agent_name}"

        if agent_name not in ["original_autogpt", "forge"]
        else agent_name
    )

    benchmark_script = os.path.join(agent_dir, "run_benchmark")

    if os.path.exists(agent_dir) and os.path.isfile(benchmark_script):
        os.chdir(agent_dir)

        subprocess.Popen([benchmark_script, *subprocess_args], cwd=agent_dir)

        click.echo(
            click.style(
                f"🚀 rodando benchmark para '{agent_name}' com argumentos de subprocesso: {' '.join(subprocess_args)}",
                
                fg="green"
            )
        )
    else:
        click.echo(
            click.style(
                f"😞 agente '{agent_name}' não existe. por favor crie o agente primeiro.",
                
                fg="red"
            )
        )

@benchmark.group(name="categories")
def benchmark_categories():
    """comando de grupo de categorias de benchmark"""

    pass

@benchmark_categories.command(name="list")
def benchmark_categories_list():
    """comando de listar as categorias de benchmark"""

    import glob
    import json
    import os

    categories = set()

    # obtém o diretório desse arquivo
    this_dir = os.path.dirname(os.path.abspath(__file__))

    glob_path = os.path.join(
        this_dir, "./benchmark/agbenchmark/challenges/**/[!deprecated]*/data.json"
    )

    # usa ele como base para o padrão glob, excluindo o diretório 'deprecated'
    for data_file in glob.glob(glob_path, recursive=True):
        if "deprecated" not in data_file:
            with open(data_file, "r") as f:
                try:
                    data = json.load(f)
                    categories.update(data.get("category", []))
                except json.JSONDecodeError:
                    print(f"erro: {data_file} não é um arquivo json válido.")

                    continue
                except IOError:
                    print(f"ioerror: o arquivo não pôde ser lido: {data_file}")

                    continue

    if categories:
        click.echo(click.style("categorias disponíveis: 📚", fg="green"))

        for category in categories:
            click.echo(click.style(f"\t📖 {category}", fg="blue"))
    else:
        click.echo(click.style("nenhuma categoria encontrada 😞", fg="red"))

@benchmark.group(name="tests")
def benchmark_tests():
    """comando de grupo de testes de benchmark"""

    pass

@benchmark_tests.command(name="list")
def benchmark_tests_list():
    """comando de listar testes de benchmark"""

    import glob
    import json
    import os
    import re

    tests = {}

    # obtém o diretório desse arquivo
    this_dir = os.path.dirname(os.path.abspath(__file__))

    glob_path = os.path.join(
        this_dir, "./benchmark/agbenchmark/challenges/**/[!deprecated]*/data.json"
    )
    
    # usa ele como base para o padrão glob, excluindo o diretório 'deprecated'
    for data_file in glob.glob(glob_path, recursive=True):
        if "deprecated" not in data_file:
            with open(data_file, "r") as f:
                try:
                    data = json.load(f)
                    category = data.get("category", [])
                    test_name = data.get("name", "")

                    if category and test_name:
                        if category[0] not in tests:
                            tests[category[0]] = []

                        tests[category[0]].append(test_name)
                except json.JSONDecodeError:
                    print(f"erro: {data_file} não é um arquivo json válido.")

                    continue
                except IOError:
                    print(f"ioerror: o arquivo não pôde ser lido: {data_file}")

                    continue

    if tests:
        click.echo(click.style("testes disponíveis: 📚", fg="green"))

        for category, test_list in tests.items():
            click.echo(click.style(f"\t📖 {category}", fg="blue"))

            for test in sorted(test_list):
                test_name = (
                    " ".join(word for word in re.split("([A-Z][a-z]*)", test) if word)
                    .replace("_", "")
                    .replace("C L I", "CLI")
                    .replace("  ", " ")
                )

                test_name_padded = f"{test_name:<40}"

                click.echo(click.style(f"\t\t🔬 {test_name_padded} - {test}", fg="cyan"))
    else:
        click.echo(click.style("nenhum teste encontrado 😞", fg="red"))

@benchmark_tests.command(name="details")
@click.argument("test_name")
def benchmark_tests_details(test_name):
    """comando de detalhes do teste de benchmark"""

    import glob
    import json
    import os

    # obtém o diretório desse arquivo
    this_dir = os.path.dirname(os.path.abspath(__file__))

    glob_path = os.path.join(
        this_dir, "./benchmark/agbenchmark/challenges/**/[!deprecated]*/data.json"
    )

    # usa ele como base para o padrão glob, excluindo o diretório 'deprecated'
    for data_file in glob.glob(glob_path, recursive=True):
        with open(data_file, "r") as f:
            try:
                data = json.load(f)

                if data.get("name") == test_name:
                    click.echo(
                        click.style(
                            f"\n{data.get('name')}\n{'-'*len(data.get('name'))}\n",

                            fg="blue"
                        )
                    )

                    click.echo(
                        click.style(
                            f"\tCategory:  {', '.join(data.get('category'))}",

                            fg="green"
                        )
                    )

                    click.echo(click.style(f"\tTask:  {data.get('task')}", fg="green"))

                    click.echo(
                        click.style(
                            f"\tdependências:  {', '.join(data.get('dependencies')) if data.get('dependencies') else 'None'}",
                            
                            fg="green"
                        )
                    )

                    click.echo(
                        click.style(f"\tcorte:  {data.get('cutoff')}\n", fg="green")
                    )

                    click.echo(
                        click.style("\tcondições de teste\n\t-------", fg="magenta")
                    )

                    click.echo(
                        click.style(
                            f"\t\tresposta: {data.get('ground').get('answer')}",

                            fg="magenta"
                        )
                    )

                    click.echo(
                        click.style(
                            f"\t\tdeve conter: {', '.join(data.get('ground').get('should_contain'))}",

                            fg="magenta"
                        )
                    )

                    click.echo(
                        click.style(
                            f"\t\tnão deve conter: {', '.join(data.get('ground').get('should_not_contain'))}",

                            fg="magenta"
                        )
                    )

                    click.echo(
                        click.style(
                            f"\t\tarquivos: {', '.join(data.get('ground').get('files'))}",

                            fg="magenta"
                        )
                    )

                    click.echo(
                        click.style(
                            f"\t\tavaliação: {data.get('ground').get('eval').get('type')}\n",

                            fg="magenta"
                        )
                    )

                    click.echo(click.style("\tinfo\n\t-------", fg="yellow"))

                    click.echo(
                        click.style(
                            f"\t\tdificuldade: {data.get('info').get('difficulty')}",

                            fg="yellow"
                        )
                    )

                    click.echo(
                        click.style(
                            f"\t\tdescrição: {data.get('info').get('description')}",

                            fg="yellow"
                        )
                    )

                    click.echo(
                        click.style(
                            f"\t\tefeitos colaterais: {', '.join(data.get('info').get('side_effects'))}",
                            
                            fg="yellow"
                        )
                    )

                    break

            except json.JSONDecodeError:
                print(f"erro: {data_file} não é um arquivo json válido.")

                continue
            except IOError:
                print(f"ioerror: o arquivo não pôde ser lido: {data_file}")

                continue

def wait_until_conn_ready(port: int = 8000, timeout: int = 30):
    """
    pesquisa pelo localhost:{port} até que esteja disponível para conexões

    parâmetros:
        port: a porta para esperar até que ela abra
        timeout: timeout em segundos; o tempo máximo de espera

    resulta:
        timeouterror: se o timeout (segundos) expirar antes da porta abrir
    """

    import socket
    import time

    start = time.time()

    while True:
        time.sleep(0.5)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("localhost", port)) == 0:
                break

        if time.time() > start + timeout:
            raise TimeoutError(f"a porta {port} não abriu em {timeout} segundos")

if __name__ == "__main__":
    cli()