# Ejercicio 3
nombre_operador = input("Ingrese su nombre (Operador): ")
while not nombre_operador.isalpha():
    nombre_operador = input("Usuario invalido, por favor ingrese su nombre (Operador): ")
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
print("Acceso permitido.")
opcion = ""
while True: # Para repetir menú
        print("")
        print("--------------------------")
        print("1. Reservar turno")
        print("2. Cancelar turno")
        print("3. Ver agenda del día")
        print("4. Ver resumen general")
        print("5. Cerrar sistema")
        print("--------------------------")
            
        opcion = input("")
        
        # Valida que sea numero y que esté dentro del rango
        if not opcion.isdigit():
            print("Ingrese solo números")
            continue
        
        if int(opcion) < 1 or int(opcion) > 5:
            print("Opción inválida")
            continue
        
        
        # Si marcan Reservar turno
        if opcion == "1":
            dia_elegido = "0"
            print("")
            print("Elige un dia.")
            print("1. Lunes")
            print("2. Martes")
            dia_elegido = input("")
            
            # Si marcan lunes se pide nombre
            if dia_elegido == "1":
                nombre_reservar = input("Ingrese su nombre y apellido (completo): ")
                # Validamos que no esté ya en algun sitio, sino se le indica que ya tiene turno
                if nombre_reservar == lunes1 or nombre_reservar == lunes2 or nombre_reservar == lunes3 or nombre_reservar == lunes4:
                    print("Este paciente ya tiene reservado turno")
                    continue

                if lunes1 == "":
                    lunes1 = nombre_reservar
                    print("¡Reserva exitosa!")

                elif lunes2 == "":
                    lunes2 = nombre_reservar
                    print("¡Reserva exitosa!")

                elif lunes3 == "":
                    lunes3 = nombre_reservar
                    print("¡Reserva exitosa!")

                elif lunes4 == "":
                    lunes4 = nombre_reservar
                    print("¡Reserva exitosa!")

                else:
                    print("No hay turnos disponibles")
                                        
            # Si marcan martes se pide nombre
            if dia_elegido == "2":
                nombre_reservar = input("Ingrese su nombre y apellido (completo): ")

                if nombre_reservar == martes1 or nombre_reservar == martes2 or nombre_reservar == martes3:
                    print("Este paciente ya tiene reservado turno")
                    continue

                if martes1 == "":
                    martes1 = nombre_reservar
                    print("¡Reserva exitosa!")

                elif martes2 == "":
                    martes2 = nombre_reservar
                    print("¡Reserva exitosa!")

                elif martes3 == "":
                    martes3 = nombre_reservar
                    print("¡Reserva exitosa!")

                else:
                    print("No hay turnos disponibles")
                
            if dia_elegido != "1" and dia_elegido != "2" and dia_elegido == "":
                print("Opcion invalida, vuelva a intentarlo.")
                continue
            
        # Si marca 2 para cancelar turno
        if opcion == "2":
            print("Ingrese el dia por favor.")
            print("1. Lunes")
            print("2. Martes")           
            dia_cancelar = input()
            nombre_cancelar = input("Por favor ingrese su nombre completo para cancelar la reserva: ")
            
            # Verifico todo directamente que sea las opciones validas , y que sean letras. 
            if not dia_cancelar.isdigit() or dia_cancelar not in ("1", "2") or not nombre_cancelar.replace(" ", "").isalpha():
                print("Datos inválidos, intente nuevamente.")
                continue
            
            # Cancelar dias lunes
            if dia_cancelar == "1":
                if lunes1 == nombre_cancelar:
                    print("Se canceló exitosamente")
                    lunes1 = ""
                elif lunes2 == nombre_cancelar:
                    print("Se canceló exitosamente")
                    lunes2 = ""
                elif lunes3 == nombre_cancelar:
                    print("Se canceló exitosamente")
                    lunes3 = ""
                elif lunes4 == nombre_cancelar:
                    print("Se canceló exitosamente")
                    lunes4 = ""
                else:
                    print("No posee turno reservado previamente")      
                    continue  
            # Cancelar dia martes        
            if dia_cancelar == "2":
                if martes1 == nombre_cancelar:
                    print("Se canceló exitosamente")
                    martes1 = ""
                elif martes2 == nombre_cancelar:
                    print("Se canceló exitosamente")
                    martes2 = ""
                elif martes3 == nombre_cancelar:
                    print("Se canceló exitosamente")
                    martes3 = ""
                else:
                    print("No posee turno reservado previamente")   
                    continue
        
        
        # Opcion 3 ver agenda completa
        if opcion == "3":
            print(f"Lunes: {lunes1 or 'libre'}, {lunes2 or 'libre'}, {lunes3 or 'libre'}, {lunes4 or 'libre'}")
            print(f"Martes: {martes1 or 'libre'}, {martes2 or 'libre'}, {martes3 or 'libre'}") 
        
        
        # Opcion 4 ver resumen general
        if opcion == "4":
            ocupados_lunes = 0
            if lunes1 != "":
                ocupados_lunes += 1
            if lunes2 != "":
                ocupados_lunes += 1
            if lunes3 != "":
                ocupados_lunes += 1
            if lunes4 != "":
                ocupados_lunes += 1

            libres_lunes = 4 - ocupados_lunes   # calculo de los libres

            ocupados_martes = 0
            if martes1 != "":
                ocupados_martes += 1
            if martes2 != "":
                ocupados_martes += 1
            if martes3 != "":
                ocupados_martes += 1

            libres_martes = 3 - ocupados_martes


            print("Resumen general:")
            print(f"Lunes → Ocupados: {ocupados_lunes} | Libres: {libres_lunes}")
            print(f"Martes → Ocupados: {ocupados_martes} | Libres: {libres_martes}")


            # Para saber cual es el mas ocupado
            if ocupados_lunes > ocupados_martes:
                print("El día con más turnos es: Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("El día con más turnos es: Martes")
            else:
                print("Hay empate en cantidad de turnos")
        
        # La unica forma de salir del loop del menú principal es esta                                
        if opcion == "5":
            print("")
            print("Hasta luego, vuelva pronto.")
            break