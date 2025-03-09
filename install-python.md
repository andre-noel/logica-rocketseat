# Como instalar o python

## Windows

1. Baixe o instalador no site oficial do Python: https://www.python.org/downloads/windows/
   Baixe a versão mais recente recomendada para Windows.
2. Execute o instalador com um duplo clique no arquivo baixado (python-<versão>.exe).
   Marque a opção `Add Python to PATH` antes de continuar!
   Clique em `Install Now` e aguarde a instalação.
3. Teste a instalação, abrindo o Prompt de Comando (cmd) ou PowerShell. Digite:

```sh
python --version
```

ou

```sh
python -V
```

Se aparecer algo como Python 3.x.x, significa que a instalação foi bem-sucedida.

## Linux (Debian, Ubuntu, Fedora e derivados)

> **Observação:** O Python já vem pré-instalado na maioria das distribuições Linux.

1. Atualize os pacotes. Abra o terminal e execute:

```sh
sudo apt update && sudo apt upgrade  # Para Debian, Ubuntu e derivados
```

ou

```sh
sudo dnf update  # Para Fedora
```

2. Instale o Python.

Para Debian, Ubuntu e derivados:

```sh
sudo apt install python3
```

Para Fedora:

```sh
sudo dnf install python3
```

3. TestE a instalação. No terminal, execute:

```sh
python3 --version
```

ou

```sh
python -V
```

Se o comando retornar Python 3.x.x, significa que a instalação foi concluída com sucesso.

## macOS

1. Usando o Homebrew (recomendado). Se ainda não tiver o Homebrew, instale-o executando no terminal:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Depois, instale o Python com:

```sh
brew install python
```

2. Teste a instalação:

```sh
python3 --version
```

ou

```sh
python -V
```

Se o comando retornar Python 3.x.x, significa que a instalação foi concluída com sucesso.
