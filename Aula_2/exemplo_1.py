#Revisão de impressão na tela

#Criação de variável
print("## Petshop TabajaraCorp ##")

#Declaração das variáveis:
nome = ""
nome_dono = ""
raca = ""
idade = 0

#Entrada de dados
nome = input("Digite o nome do cusco: ")
nome_dono = input("Digite o nome do dono: ")
raca = input("Digite a raça do cusco: ")
idade = int(input("Digite a idade do cusco: "))

print("_____________________________________________________________\n")

#Saída dos dados
print(f"Nome do cusco: {nome}")
print(f"Nome do dono do cusco: {nome_dono}")
print(f"Raça do cusco: {raca}")
print(f"Idade do cusco: {idade}")

print("______________________________________________________________\n")

#print("Outra forma de Mostrar os dados" )
print(f"Nome do cusco: {nome}, Raça: {raca}, Idade: {idade}, dono: {nome_dono}")

print("______________________________________________________________\n")
#print("Outra forma de Mostrar os dados: Concatenando" )
#Para a concatenação, é possível usar "," ou "+"
print("Nome do cusco: ",nome)
print("Nome do dono: ",nome_dono)
print("Raça do cusco: ",raca)
print("Idade do cusco: ",idade)
