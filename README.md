# Conversor de Bases

Este é um programa simples em Python que permite a conversão entre diferentes bases numéricas: Binário, Hexadecimal e Decimal. Ele apresenta um menu interativo para o usuário escolher a operação desejada e exibe os resultados de forma prática.

## Funcionalidades

O programa suporta as seguintes conversões:
1. Inteiro para Binário
2. Binário para Inteiro
3. Inteiro para Hexadecimal
4. Hexadecimal para Inteiro

## Como usar

1. Execute o arquivo `main.py`.
2. Escolha uma das opções do menu:
   - **Inteiro para Binário**: Insira um número inteiro e veja sua representação em binário.
   - **Binário para Inteiro**: Insira um número binário (sem prefixo) e veja o número correspondente em inteiro.
   - **Inteiro para Hexadecimal**: Insira um número inteiro e veja sua representação em hexadecimal (em letras maiúsculas).
   - **Hexadecimal para Inteiro**: Insira um número hexadecimal (sem prefixo) e veja o número correspondente em inteiro.
   - **Sair**: Encerre o programa.
3. Siga as instruções exibidas no console.

## Exemplo de Uso

### Conversão de Inteiro para Binário

Digite um número inteiro: 10 
Binário: 1010

### Conversão de Binário para Inteiro

Digite o número binário: 1010 
Inteiro: 10


## Requisitos

- Python 3.6 ou superior.

## Estrutura do Código

- `inteiro_para_binario(numero)`: Converte um número inteiro para binário.
- `binario_para_inteiro(binario)`: Converte um número binário para inteiro.
- `inteiro_para_hexa(numero)`: Converte um número inteiro para hexadecimal.
- `hexa_para_inteiro(hexa)`: Converte um número hexadecimal para inteiro.
- `receber_inteiro(mensagem)`: Valida e recebe a entrada de um número inteiro do usuário.
- `exibir_menu()`: Exibe o menu interativo para o usuário.
- `main()`: Função principal que gerencia o fluxo do programa.

## Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e correções. 
