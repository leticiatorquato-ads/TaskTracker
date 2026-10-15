def cadastrar_tarefa(lista):
    print("\n" + "-"*30)
    print("      NOVO CADASTRO")
    print("-"*30)

    while True:
        titulo = input("Título da tarefa (obrigatório): ").strip()
        if titulo != "":
            break
        print("⚠️ Erro: O título não pode ficar em branco. Tente novamente.")

    descricao = input("Descrição: ").strip()

    while True:
        prioridade_input = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if prioridade_input in ["alta", "média", "media", "baixa"]:
            prioridade = prioridade_input.capitalize()
            break
        else:
            print("⚠️ Erro: Prioridade inválida. Digite exatamente Alta, Média ou Baixa.")

    data_limite = input("Data Limite (ex: 15/10/2026 ou 'Amanhã'): ").strip()

    tarefa = {
        "Título": titulo,
        "Descrição": descricao,
        "Prioridade": prioridade,
        "Data Limite": data_limite,
        "Status": "Pendente"
    }

    lista.append(tarefa)
    print("\n✅ Tarefa cadastrada com sucesso!")


def visualizar_tarefas(lista):
    print("\n" + "-"*30)
    print("      LISTA DE TAREFAS")
    print("-"*30)

    # Validação de Lista Vazia
    if len(lista) == 0:
        print("📭 Nenhuma tarefa cadastrada no momento.")
    else:
        # Itera sobre a lista preenchida
        for indice, tarefa in enumerate(lista, start=1):
            print(f"\n📌 TAREFA #{indice}")
            print(f"   Título      : {tarefa['Título']}")
            print(f"   Descrição   : {tarefa['Descrição']}")
            print(f"   Prioridade  : {tarefa['Prioridade']}")
            print(f"   Data Limite : {tarefa['Data Limite']}")
            print(f"   Status      : {tarefa['Status']}")
        print("\n" + "-"*30)


def main():
    lista_de_tarefas = []

    while True:
        print("\n" + "="*30)
        print("      MENU DE TAREFAS")
        print("="*30)
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")

        opcao = input("\nEscolha uma opção (1, 2 ou 3): ").strip()

        if opcao == '1':
            cadastrar_tarefa(lista_de_tarefas)

        elif opcao == '2':
            visualizar_tarefas(lista_de_tarefas)

        elif opcao == '3':
            print("\nEncerrando a aplicação... Até logo!")
            break

        else:
            print("\n⚠️ Opção inválida! Por favor, digite apenas 1, 2 ou 3.")

if __name__ == "__main__":
    main()