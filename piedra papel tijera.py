nombre1 = input ("¿Como se llama el jugador 1")
nombre2 = input ("¿Como se llama el jugador 2")

jugador1 = input("Elige piedra, papel o tijera: ")
jugador2 = input("Elige piedra, papel o tijera: ")

condition1 = jugador1 == "piedra" and jugador2 == "tijera"
condition2 = jugador1 == "papel" and jugador2 == "piedra"
condition3 = jugador1 == "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
    print("¡Ha sido un empate!")
elif condition1 or condition2 or condition3:
    print('Ha ganado', nombre1)
else:
    print('Ha ganado', nombre2)
