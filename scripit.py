nome = input ("Digite seu nome: ")
idade = int(input ("Digite sua idade: "))
print(nome)

if idade >17:
    print (" VOcê pode entrar no site!")
else:
    print ("Acesso bloqueado!")

with open ("base_dados.csv", "a") as arquivo: 
    arquivo.write(f"Seja bem vindo(a){nome}.\n")
