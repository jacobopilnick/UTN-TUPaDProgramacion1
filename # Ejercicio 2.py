# Ejercicio 2
USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"
# Contador de intentos
intentos = 0

usuario = input("Por favor ingrese el usuario: ")
clave = input("Por favor ingrese la contraseña: ")

# El while es para definir si le deja ingresar o no
while intentos < 3:
    if usuario != USUARIO_CORRECTO or clave != CLAVE_CORRECTA:
        intentos += 1   # Sumo contador por cada error y pido nuevamente las credenciales
        usuario = input("Por favor ingrese el usuario: ")
        clave = input("Por favor ingrese la contraseña: ")
        # Si llego a que el contador de intentos sea 2 (que contando el primer intento fuera del while seria el tercer intento), procedo a bloquear acceso y cerrar todo.
        if intentos == 2:
            print("Usuario bloqueado.")
            break
    # En caso de tener bien las credenciales le dejo ingresar y ver el menú de inicio.
    if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRECTA:
        opcion = " "
        while not opcion.isdigit(): # Valido con isdigit como se solicitó, tuve que colocar mi variable opcion como string, ya que solo toma string el isdigit, yo la tenia como numeros.
            print("--------------------------")
            print("1. Estado de inscripción")
            print("2. Cambiar clave")
            print("3. Frase motivacional")
            print("4. Salir")
            print("--------------------------")
            
            opcion = input("")
        # Dependiendo de cual de las opciones validas marque el usuario, se hará una u otra operacion lógica
            if opcion == "1":
                print("")
                print("Inscripto")
                
            if opcion == "2":
                print("")
                clave_nueva = input("Ingrese la nueva clave (minimo 6 caracteres): ")
                while len(clave_nueva) < 6: # Uso de len para repetir siempre que sea menor a 6 caracteres la nueva clave
                    print("")
                    clave_nueva = input("Ingrese la nueva clave (minimo 6 caracteres): ")
                if len(clave_nueva) >= 6: # En caso de cumplir el requisito, pido que repita la contraseña para confirmar
                    print("")
                    clave_confirmacion = input("Por favor repita la contraseña: ")
                    while clave_confirmacion != clave_nueva: # Si la contraseña nueva no coincide con la contraseña de confirmacion, le pido que repita nada mas la de confirmacion
                        print("")
                        clave_confirmacion = input("Por favor repita la contraseña: ")
                        
            if opcion == "3":
                print("")
                print(" \"Cada hora de estudio que hoy te exige, mañana te acerca a un futuro donde tu conocimiento se transforma en oportunidades, crecimiento y éxito real.\"")
        
        # La opcion 4 es la que hace que el primer while de todos no sea infinito, y tenga forma de salir el usuario de la plataforma.    
        if opcion == "4":
            print("")
            print("Hasta luego, vuelva pronto.")
            break