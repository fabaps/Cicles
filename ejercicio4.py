import random
n = int(input("Ingrese un numero: "))
if n>0:
  lista = []
  cont = 0
  while cont < n:
    numero = random.randint(1,100)
    print("El numero generado es: ", numero  )
    lista.append(numero)
    print(lista)
    cont += 1
else: 
  print("Debe ingresar un numero entero mayor a 0")
