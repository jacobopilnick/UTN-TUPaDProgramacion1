# Ejercicio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0

# nombre agente en letras
nombre = input("Ingrese su nombre de agente: ")
while not nombre.isalpha():
    nombre = input("Nombre inválido. Ingrese solo letras: ")

print(f"Bienvenido agente {nombre}. Iniciando misión...")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # Bloqueo de alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado por alarma. DERROTA.")
        break

    # Voy actualizando los stats
    print("\nEstado actual:")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {alarma}")
    print(f"Código parcial: {codigo_parcial}")

    # Menu de accion
    print("\n1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")
    
    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
        opcion = input("Opción inválida. Seleccione 1, 2 o 3: ")

    # Opcion 1 forzar
    if opcion == "1":
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        # Antispam
        if forzar_seguidas == 3:
            print("Forzaste 3 veces seguidas. La cerradura se trabó.")
            alarma = True
            forzar_seguidas = 0
            continue

        # Alerta de alarma
        if energia < 40:
            print("Riesgo de alarma. Elegí un número del 1 al 3:")
            num = input()

            while not num.isdigit() or num not in ("1", "2", "3"):
                num = input("Número inválido. Ingrese 1, 2 o 3: ")

            if num == "3":
                alarma = True
                print("Se activó la alarma.")

        if not alarma:
            cerraduras_abiertas += 1
            print("Abriste una cerradura.")

    # Opcion 2 hackear
    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0

        print("Hackeando...")
        for i in range(4):
            print(f"Progreso: {i+1}/4")
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Código completado. Se abrió una cerradura.")

    # Opcion 3 descansar
    elif opcion == "3":
        tiempo -= 1
        forzar_seguidas = 0

        if alarma:
            energia -= 10
            print("Descansaste, pero la alarma consume energía.")

        energia += 15
        if energia > 100:
            energia = 100

# Final de todo
if cerraduras_abiertas == 3:
    print("\nVICTORIA: Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("\nDERROTA: Te quedaste sin recursos.")