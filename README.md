# TaskTracker 📝

## Descrição Funcional
O **TaskTracker** é uma aplicação interativa de linha de comando (CLI) desenvolvida para o gerenciamento de tarefas do dia a dia. O sistema opera em um loop contínuo e permite que o usuário gerencie suas atividades de forma rápida diretamente pelo terminal.

### Principais Funcionalidades:
- **Cadastro de Tarefas:** Permite inserir novas tarefas informando Título, Descrição, Prioridade e Data Limite.
- **Validação Inteligente:** O sistema não permite cadastrar tarefas sem título e aceita apenas níveis de prioridade válidos (Alta, Média ou Baixa).
- **Listagem Organizada:** Exibe todas as tarefas cadastradas de forma estruturada e legível, alertando o usuário caso a lista esteja vazia.

---

## Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Dependências:** O projeto utiliza puramente a biblioteca padrão do Python, não sendo necessária a instalação de pacotes externos.

---

## Guia de Instalação e Execução (Local)

### Pré-requisitos
Para executar este projeto localmente, você precisa ter o Python (versão 3.10 ou superior) instalado em sua máquina.

### Como executar
1. Faça o clone deste repositório:
   ```bash
   git clone https://github.com/leticiatorquato-ads/TaskTracker.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd TaskTracker
   ```
3. Execute a aplicação:
   ```bash
   python src/main.py
   ```

## 🐳 Execução com Docker (Fase 3)

Instruções para construir e executar a aplicação em ambiente conteinerizado.

Pré-requisitos
- Docker Desktop instalado e rodando na máquina.

Comandos de Execução

Construir a imagem Docker:
   ```bash
   docker build -t tasktracker-app .
   ```

Executar a aplicação via Docker Compose:
   ```bash
   docker compose run tasktracker-app
   ```