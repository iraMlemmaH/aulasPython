#DESAFIO: Criar um cadastro completo!
#Deve conter: Nome, sobrenome, idade, sexo, endereço, bairro, cidade, estado, telefone, cpf, rg e email. 
#Mostrar os dados solicitados utilizando as diversas formas de impressão e utilize concatenação. print("Nome do dono:", nome_dono)

#author: ✧Mari✧
print("•–––––----–☆––––-----––•")
print("       [ CADASTRO ]")
print("•–––––----–☆––––-----––•\n")

print("Por favor, digite:")
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
idade = int(input("Idade: "))
bairro = input("Bairro: ")
cidade = input("Cidade: ")
estado = input("Estado: ")
telefone = input("Telefone: ")
cpf = input("CPF: ")
rg = input("RG: ")
email = input("Email: ")
print(" \n•–––––----–☆––––-----––•\n\n")

# print(f"Você se chama",nome,sobrenome,".")
# print(f"Tem {idade} anos, reside no bairro {bairro}, que fica localizado na cidade de {cidade}, no estado {estado}.")  
# print(f"\nTelefone: ",telefone,"\nCPF: ",cpf,"\nRG:",rg,"\nEmail:",email,".")

print(f"Você se chama",nome,sobrenome,". Tem {idade} anos, reside no bairro {bairro}, que fica localizado na cidade de {cidade}, no estado {estado}.\nTelefone: ",telefone,"\nCPF: ",cpf,"\nRG:",rg,"\nEmail:",email,".")