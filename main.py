import random
print ("¡Hello world!")
#1 dos jugadores
#2 cada jugador elige con que jugar
#3 tres opciones: piedra, papel o tijeras
#4 muestran su elección
#5 deciden quien es el ganador

# Dar las instrucciones

print ("Juguemos piedra, papel o tijeras")
opcion=input("¿Cuál es tu opción? ")
print(opcion)  

#Hacer validación del input
#La computadora elige un valor para hacer la comparación

opciones=["piedra","papel","tijeras"]
eleccion=random.choice(opciones)
print(eleccion)

#Elegir el ganador

if opcion==eleccion:
    print("Empate")
elif opcion=="piedra" and eleccion=="papel":
    print("Gana la computadora")
elif opcion=="piedra" and eleccion=="tijeras":
    print("Gana el jugador")
elif opcion=="papel" and eleccion=="piedra":
    print("Gana el jugador")
elif opcion=="papel" and eleccion=="tijeras":
    print("Gana la computadora")
elif opcion=="tijeras" and eleccion=="papel":
    print("Gana el jugador")
elif opcion=="tijeras" and eleccion=="piedra":
    print("Gana la computadora")
else:
    print("Perdiste porque esa opción no existe")
