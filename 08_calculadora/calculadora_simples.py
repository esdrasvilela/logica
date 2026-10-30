from cores import *

num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))


def menu():
    print(f"\n" + FRENTE_PRETO + FUNDO_VERDE_CLARO + "_____MENU_____" + RESET)
    
    print(f""+ FRENTE_VERMELHO_CLARO + "1 " + RESET + FRENTE_CIANO_CLARO + "- Soma " + RESET)
    print(f""+ FRENTE_VERMELHO_CLARO + "2 " + RESET + FRENTE_CIANO_CLARO + "- Subtrair " + RESET)
    print(f""+ FRENTE_VERMELHO_CLARO + "3 " + RESET + FRENTE_CIANO_CLARO + "- Multiplicar " + RESET)
    print(f""+ FRENTE_VERMELHO_CLARO + "4 " + RESET + FRENTE_CIANO_CLARO + "- Dividir " + RESET)
    print(f""+ FRENTE_VERMELHO_CLARO + "5 " + RESET + FRENTE_CIANO_CLARO + "- Sair " + RESET)



def somar():
    resultadoSomar = num1 + num2
    print(f"O Resultado da Soma de {num1} + {num2} é: {resultadoSomar}")

def subtrair():
    resultadoSub = num1 - num2
    print(resultadoSub)

def multiplicar():
    resultadoMulti = num1 * num2
    print(resultadoMulti)

def dividir():
    if num2 == 0:
        print("Não é possível dividir por zero!")
    else:
        resultadoDiv = num1 / num2
        print(resultadoDiv)




opcao = ""
while opcao != "5":
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
        print("Até logo!")
    else:
        print("Operador Inválido!")
