# Criando uma nova lista
lista = [
    "Gabriel",
    "Vinicius",
    "Jussara",
    "Priscilla",
    "Maurício",
    "Josiane"
]

# adicionando itens a lista ja criada
lista.append("Felipe")
lista_extra = ["Jeremias", "Pindamonhangabo"]
print(f"\n {lista}")
print(f"\n {lista[0]}")
lista.extend(lista_extra)
print(f"\n {lista}")

# Adicionando novos itens através do método input


lista.append(input("Insira um nome: "))
print(f"\nNova Lista: {lista}")

# Tirando itens da lista através do método .pop()
# Também é possivel usar remove para tirar o ultimo item da lista
# Ou popleft
lista.pop(2) 
print(f"\n\nNova Lista: {lista}")
