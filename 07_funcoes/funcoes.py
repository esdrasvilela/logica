#Função sem retorno e sem parâmetros
def sobre():
     print("Desenvolvido por: Esdras Vilela")
# Função SEM RETORNO e com parâmetros

def turma(turma, ano):
    print(f"Turma: {turma}, {ano}")



#Função com retorno e Com parâmetros

def somar(numero1, numero2):
    return numero1 + numero2

sobre()
turma("AD_05", 2026)

resultado = somar(10, 5)
print(f"A soma de 10 + 5 = {resultado}")

