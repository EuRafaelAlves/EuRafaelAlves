#proxíma aula realizar parte 3 e 4

#Um caixa registrador precissa retornar o número de notas correto (Notas de 1, 2, 5, 10, 20, 50, 100, 200); faça um programa em python e receba um valor de saque inteiro e imprime
#o número de notas respectivo 
# // Divisão inteira

saque = input("Digite o valor que deseja sacar: ")

int_saque = int(saque)
notas_200 = int_saque // 200 
resto_nota_200 = int_saque % 200

notas_100 = resto_nota_200 // 100
resto_nota_100 = resto_nota_200  % 100

notas_50 = resto_nota_100 // 50
resto_nota_50 = resto_nota_100 % 50

notas_20 = resto_nota_50 // 20
resto_nota_20 = resto_nota_50 % 20

notas_10 = resto_nota_20 // 10
resto_nota_10 = resto_nota_20 % 10

notas_5 = resto_nota_10 // 5
resto_nota_5 = resto_nota_10 % 5

notas_2 = resto_nota_5 // 2
resto_nota_2 = resto_nota_5 % 2

notas_1 = resto_nota_2 // 1
resto_nota_1 = resto_nota_2 * 1




print("Notas de 200: ", notas_200)
print("Notas de 100: ", notas_100)
print("Notas de 50: ", notas_50)
print("Notas de 20: ", notas_20)
print("Notas de 10: ", notas_10)
print("Notas de 5: ", notas_5)
print("Notas de 2: ", notas_2)
print("Notas de 1: ", notas_1)