## Contexto
# Mad Lib é um jogo de palavras. Uma pessoa pede ao grupo palavras soltas (um nome, um adjetivo, uma comida...) sem contar para que servem. Depois, ela encaixa tudo nos espaços em branco de uma história pronta, e o resultado costuma ser bem engraçado.

# Neste projeto, o seu programa assume o papel de quem conduz o jogo.
nome = input("Digite o seu nome: ")
profissao = input("Digite o nome do seu curso: ")
adj1 = input("Em uma palavra, de um adjetivo para o que você achou da sua turma na generation!:")
adj2 = input("Em uma palavra, de um adjetivo para o que você achou do instrutor: ")
comida1 = input("Digite uma comida que voce comeu no almoço: ")
comida2 = input("Digite outra coisa do seu almoço: ")
sentimento = input("Escreva como você se sente: ")


print(f"\n\n\n{nome} começou hoje o seu primeiro curso na Generation Brasil.\nEstá cursando a formação em {profissao}\nAchou a sua turma muito {adj1} \nmas o instrutor era, no mínimo, {adj2} \nNo almoço, comeu {comida1} e {comida2} enquanto revisava as suas anotações.\nAo final do dia, sente-se {sentimento}, mas tem a determinação de concluir a jornada.")