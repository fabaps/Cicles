string = input("Ingrese una palabra: ")
ch = input("Ingrese el caracter a buscar: ")
lista =[]
i = 0
for cont in range(0,len(string)):
  if string[cont] == ch:
    lista.append(cont)
    i += 1
print (lista)
print ("Existencias = ", i)





    