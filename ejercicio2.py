import random
n = random.randint(4,8)
print("BIENVENIDO AL JUEGO USUARIO. DESPLEGAREMOS UN NUMERO Y TU TIENES QUE ADIVINAR QUE COLOR TIENE ESA CANTIDAD DE LETRAS. TIENES 5 OPORTUNIDADES PARA ADIVINAR. ")
print("----------------------------------------")
print("¿Que color tiene esta cantidad de letras? ", n)

color = input("Ingrese respuesta: ")
cont = 1
i = 4
lg = len(color)
st =""
while cont < 5:
  if lg == n:
    print(st)
    print("¡¡Felicidades ganaste!!")
    break 
  else:
    print(st)
    print("****TIENES ",i-0, "INTENTOS****")
    i -= 1
    color = input("Ingrese respuesta: ")
  cont +=1
else:
  print(st)
  print("SE ACABARON TUS 5 VIDAS PARA ADIVINAR")
  print("Saliendo...")












