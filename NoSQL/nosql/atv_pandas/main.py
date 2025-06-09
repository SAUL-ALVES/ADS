from cliente_dao import ClienteDAO
from models import Cliente


def exibir_cliente(cliente: Cliente):
    print(vars(cliente))


def main():
    dao = ClienteDAO("csv/german_credit_data.csv")

    while True:
        print("\n======= MENU =======")
        print("1 - Listar todos os clientes")
        print("2 - Criar novo cliente")
        print("3 - Buscar cliente por ID")
        print("4 - Atualizar cliente")
        print("5 - Remover cliente")
        print("6 - Filtrar por aprovação")
        print("7 - Estatísticas de crédito")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nTabela completa:")
            print(dao.df.to_string(index=False))

        elif opcao == "2":
            try:
                idade = int(input("Idade: "))
                sexo = input("Sexo (male/female): ")
                credito = int(input("Crédito: "))
                moradia = input("Moradia (own/free/rent): ")
                poupanca = input("Conta poupança: ")
                corrente = input("Conta corrente: ")
                duracao = int(input("Duração: "))
                proposito = input("Propósito: ")
                aprovacao = int(input("Aprovação (1 ou -1): "))

                cliente = Cliente(
                    idade=idade,
                    sexo=sexo,
                    credito=credito,
                    moradia=moradia,
                    conta_poupanca=poupanca,
                    conta_corrente=corrente,
                    duracao=duracao,
                    proposito=proposito,
                    aprovacao=aprovacao,
                )
                cliente_criado = dao.criar(cliente)
                print(f"\nCliente criado com ID: {cliente_criado.id}")
            except Exception as e:
                print("Erro:", e)

        elif opcao == "3":
            id_cliente = int(input("ID do cliente: "))
            cliente = dao.buscar_por_id(id_cliente)
            if cliente:
                exibir_cliente(cliente)
            else:
                print("Cliente não encontrado.")

        elif opcao == "4":
            id_cliente = int(input("ID do cliente para atualizar: "))
            cliente = dao.buscar_por_id(id_cliente)
            if not cliente:
                print("Cliente não encontrado.")
                continue

            print("Pressione ENTER para manter o valor atual.")
            idade = input(f"Idade ({cliente.idade}): ") or cliente.idade
            sexo = input(f"Sexo ({cliente.sexo}): ") or cliente.sexo
            credito = input(f"Crédito ({cliente.credito}): ") or cliente.credito
            moradia = input(f"Moradia ({cliente.moradia}): ") or cliente.moradia
            poupanca = (
                input(f"Poupança ({cliente.conta_poupanca}): ")
                or cliente.conta_poupanca
            )
            corrente = (
                input(f"Corrente ({cliente.conta_corrente}): ")
                or cliente.conta_corrente
            )
            duracao = input(f"Duração ({cliente.duracao}): ") or cliente.duracao
            proposito = input(f"Propósito ({cliente.proposito}): ") or cliente.proposito
            aprovacao = input(f"Aprovação ({cliente.aprovacao}): ") or cliente.aprovacao

            cliente.idade = int(idade)
            cliente.sexo = sexo
            cliente.credito = int(credito)
            cliente.moradia = moradia
            cliente.conta_poupanca = poupanca
            cliente.conta_corrente = corrente
            cliente.duracao = int(duracao)
            cliente.proposito = proposito
            cliente.aprovacao = int(aprovacao)

            if dao.atualizar(cliente):
                print("Cliente atualizado com sucesso.")
            else:
                print("Erro ao atualizar.")

        elif opcao == "5":
            id_cliente = int(input("ID do cliente a remover: "))
            if dao.remover(id_cliente):
                print("Cliente removido.")
            else:
                print("Cliente não encontrado.")

        elif opcao == "6":
            status = int(input("Aprovação (1 = aprovados, -1 = reprovados): "))
            for cliente in dao.filtrar_por_aprovacao(status):
                exibir_cliente(cliente)

        elif opcao == "7":
            print("\nEstatísticas de Crédito:")
            for k, v in dao.estatisticas_credito().items():
                print(f"{k}: {v}")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
