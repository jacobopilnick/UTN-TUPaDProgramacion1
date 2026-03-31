# Ejercicio 5
print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_jugador = True

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:

    print("\n=== NUEVO TURNO ===")
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    # Menu de accion
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")

    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    # Ataque pesado
    if opcion == "1":
        if vida_enemigo < 20:
            danio = danio_pesado * 1.5  # float
            print("¡Golpe crítico!")
        else:
            danio = danio_pesado

        vida_enemigo -= danio
        print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

    # Rafaga veloz
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    # Curar
    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Te curaste 30 puntos de vida.")
        else:
            print("¡No quedan pociones!")

    # Enemigo
    if vida_enemigo > 0:  # Evita ataque si ya lo mataste
        vida_jugador -= danio_enemigo
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

# Resultados
if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")