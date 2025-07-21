#!/bin/bash

if [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    echo "esse script não pode ser executado no windows."
    echo "siga as instruções de instalação em https://docs.python.org/3/using/windows.html"
    echo "para instalar o poetry no windows, siga as instruções em https://python-poetry.org/docs/master/#installation"
    
    exit 1
else
    if ! command -v python3 &> /dev/null

    then
        echo "python3 não foi encontrado"
        echo "instalar o python3 utilizando o pyenv ([y]/n)?"

        read response

        if [[ "$response" == "y" || -z "$response" ]]; then
            echo "instalando python3..."

            if ! command -v pyenv &> /dev/null

            then
                echo "pyenv não foi encontrado"
                echo "instalando o pyenv..."

                curl https://pyenv.run | bash
            fi

            pyenv install 3.11.5
            pyenv global 3.11.5
        else
            echo "abortando a configuração"

            exit 1
        fi
    fi

    if ! command -v poetry &> /dev/null

    then
        echo "poetry could not be found"
        echo "instalar o poetry utilizando seu instalador oficial ([y]/n)?"

        read response

        if [[ "$response" == "y" || -z "$response" ]]; then
            echo "instalando o poetry..."

            curl -sSL https://install.python-poetry.org | python3 -
        else
            echo "abortando a configuração"

            exit 1
        fi
    fi
fi