def inteiro_para_binario(numero):
    return bin(numero)[2:]

def binario_para_inteiro(binario):
    return int(binario, 2)

def inteiro_para_hexa(numero):
    return hex(numero)[2:].upper()

def hexa_para_inteiro(hexa):
    return int(hexa, 16)

def receber_inteiro(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        print("Por favor, insira um número válido.")
        return None

def exibir_menu():
    menu = """
    === Conversor de Bases ===
    1. Inteiro para Binário
    2. Binário para Inteiro
    3. Inteiro para Hexadecimal
    4. Hexadecimal para Inteiro
    5. Sair
    """
    print(menu)
    return input("Escolha uma opção: ")

def main():
    while True:
        opcao = exibir_menu()
        if opcao == "1":
            numero = receber_inteiro("Digite um número inteiro: ")
            if numero is not None:
                print(f"Binário: {inteiro_para_binario(numero)}")
        elif opcao == "2":
            binario = input("Digite o número binário: ")
            print(f"Inteiro: {binario_para_inteiro(binario)}")
        elif opcao == "3":
            numero = receber_inteiro("Digite um número inteiro: ")
            if numero is not None:
                print(f"Hexadecimal: {inteiro_para_hexa(numero)}")
        elif opcao == "4":
            hexa = input("Digite o número hexadecimal: ")
            print(f"Inteiro: {hexa_para_inteiro(hexa)}")
        elif opcao == "5":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
