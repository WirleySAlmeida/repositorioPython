#   Faça um programa que vai lendo do teclado uma sequência
#   de números inteiros terminadas por zero e, quando o
#   usuário digita o zero, ele imprime essa sequência na
#   ordem inversa

print("Digite uma sequência de números inteiros terminados por zero.")
print("A sequência termina quando o usuario digita zero.")
n = int(input())
lista = [n]

while n != 0 and (n % 10 == 0):
    n = int(input("Próximo número da sequência: "))
    lista.append(n)

tam = len(lista) - 2
while tam >= 0:
    print(lista[tam])
    tam = tam - 1
