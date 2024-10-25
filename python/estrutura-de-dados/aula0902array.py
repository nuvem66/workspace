#Array (vetor) 10 posições
lista = [1,2,3,4,5,6,7,8,9,0]
print(f"Minha lista: {lista}\n")

#Mostre a posição 6 do array
print(lista[6])
#Também pode ser exibido da seguinte forma:
n = 6
print(f"Valor {n} da minha lista: {lista[n]}") #Ajuda a manutenção do código!

#Modificando o valor da posição 3
lista[3] = 100
print(f"Minha lista modificada: {lista}")

#Adicionando um valor ao final da lista
lista.append(99)
print(f"Minha lista com um novo valor: {lista}")

#Deletando o valor da posição N
del lista[2]
print(f"Minha lista com um valor a menos {lista}")

#CRUD = Create Read Update Delete 
