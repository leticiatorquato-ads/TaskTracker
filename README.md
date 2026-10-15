# TaskTracker 📝

## Descrição Funcional

O **TaskTracker** é uma aplicação interativa de linha de comando (CLI) desenvolvida para o gerenciamento de tarefas do dia a dia. O sistema opera em um loop contínuo e permite que o usuário gerencie suas atividades de forma rápida diretamente pelo terminal.

**Principais Funcionalidades:**

* **Cadastro de Tarefas:** Permite inserir novas tarefas informando Título, Descrição, Prioridade e Data Limite.

* **Validação Inteligente:** O sistema não permite cadastrar tarefas sem título e aceita apenas níveis de prioridade válidos (Alta, Média ou Baixa).

* **Listagem Organizada:** Exibe todas as tarefas cadastradas de forma estruturada e legível, alertando o usuário caso a lista esteja vazia.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Dependências:** O projeto utiliza puramente a biblioteca padrão do Python, não sendo necessária a instalação de pacotes externos (como `pip install`).

## Guia de Instalação e Execução

### Pré-requisitos

Para executar este projeto, você precisa ter o [Python](https://www.python.org/downloads/) (versão 3.10 ou superior) instalado em sua máquina.

### Como executar

1. Faça o clone deste repositório ou baixe os arquivos para o seu computador:
   ```bash
   git clone https://github.com/seu-usuario/TaskTracker.git
   ```

2. Abra o terminal e navegue até a pasta do projeto:
   ```bash
   cd TaskTracker
   ```

3. Execute o arquivo principal da aplicação:
   ```bash
   python src/main.py
   ```
   *(Nota: No macOS ou Linux, pode ser necessário utilizar o comando `python3 src/main.py`).*
