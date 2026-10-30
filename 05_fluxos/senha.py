senha = ""
contador = 0

while senha != "turmaad05" and contador <4:
    if contador > 0:
        print(f"Senha incorreta. {4 - contador} tentativa(s) restante(s).")
    senha = input("Digite a senha: ")
    contador += 1
if senha == "turmaad05":
    print("Acesso permitido.")
else:
    print("Acesso negado.")