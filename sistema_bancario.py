def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("⚠️ Valor inválido para depósito.")
    return saldo, extrato


def sacar(saldo, extrato, valor, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > limite:
        print(f"❌ O limite de saque é R$ {limite:.2f}.")
    elif numero_saques >= limite_saques:
        print("❌ Limite diário de saques atingido.")
    elif valor <= 0:
        print("⚠️ Valor inválido para saque.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print("Nenhuma movimentação realizada." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================\n")


def menu():
    print("""
========== MENU ==========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==========================
""")


# Função principal
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        menu()
        opcao = input("Escolha uma opção: ").lower()

        if opcao == "d":
            valor = float(input("Valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == "s":
            valor = float(input("Valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo, extrato, valor, limite, numero_saques, LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("👋 Saindo do sistema bancário...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


# Executa o programa
main()
