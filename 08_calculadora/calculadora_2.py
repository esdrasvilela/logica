from cores import *


def inserirNumeros():
    num1 = float(input("Insira um número: "))
    num2 = float(input("Insira outro número: "))
    return num1, num2

num1, num2 = inserirNumeros()

def menu():
    print(f"\n" + FRENTE_PRETO + FUNDO_VERDE + f"Primeiro Numero = {num1}" + RESET + "\n" + RESET + FRENTE_PRETO + FUNDO_VERDE + f"Segundo número {num2}" + RESET )
    print(f"\n" + FRENTE_PRETO + FUNDO_VERDE_CLARO + "_____MENU_____" + RESET)
    
    print(f""+ FRENTE_VERMELHO_CLARO + "1 " + RESET + FRENTE_CIANO_CLARO + "- Soma " + RESET)
    print(f""+ FRENTE_VERMELHO_CLARO + "2 " + RESET + FRENTE_CIANO_CLARO + "- Subtrair " + RESET)
    print(f""+ FRENTE_VERMELHO_CLARO + "3 " + RESET + FRENTE_CIANO_CLARO + "- Multiplicar " + RESET)
    print(f""+ FRENTE_VERMELHO_CLARO + "4 " + RESET + FRENTE_CIANO_CLARO + "- Dividir " + RESET)
    print(f""+ FRENTE_VERMELHO_CLARO + "5 " + RESET + FRENTE_CIANO_CLARO + "- Mudar Números " + RESET)
    print(f""+ FRENTE_VERMELHO_CLARO + "6 " + RESET + FRENTE_CIANO_CLARO + "- Sair " + RESET)



def somar():
    resultadoSomar = num1 + num2
    print(FRENTE_VERDE_CLARO + FUNDO_CINZA + f"O Resultado da Soma de {num1} + {num2} é: {resultadoSomar} " + RESET)

def subtrair():
    resultadoSub = num1 - num2
    print(FRENTE_VERDE_CLARO + FUNDO_CINZA + f"O Resultado da Subtração de {num1} - {num2} é: {resultadoSub}" + RESET)

def multiplicar():
    resultadoMulti = num1 * num2
    print(FRENTE_VERDE_CLARO + FUNDO_CINZA + f"O Resultado da Multiplicação de {num1} x {num2} é: {resultadoMulti}" + RESET)

def dividir():
    resultadoDiv = num1 / num2
    print(FRENTE_VERDE_CLARO + FUNDO_CINZA + f"O Resultado da Divisão de {num1} dividido por {num2} é: {resultadoDiv}" + RESET)




opcao = ""
while opcao != "6":
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao =="1":
        somar()
    elif opcao == "2":
        subtrair() 
    elif opcao == "3":
        multiplicar() 
    elif opcao == "4":
        dividir() 
    elif opcao == "5":
        inserirNumeros() 
    elif opcao == "6":
        print("Até logo!")
    else:
        print("Opção Inválida!")
