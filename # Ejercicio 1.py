# Ejercicio 1
nombre_cliente = input("Por favor, ingrese su nombre: ")

# Valida que sea letras
while not nombre_cliente.isalpha():
    print("Error: solo se permiten letras y no puede estar vacio. ")
    nombre_cliente = input("Por favor, ingrese su nombre: ")
    
# Una vez tiene un nombre valido, pide la cantidad de productos
cantidad_productos_a_comprar = input(f"Ingrese la cantidad de productos a comprar, {nombre_cliente}: ")

# Valida que la cantidad de prodcuto sea un numero y que sea superior a tambien
while (cantidad_productos_a_comprar == "0") or not cantidad_productos_a_comprar.isdigit():
      print("Error: no puede ingresar numeros inferiores a 1.")
      cantidad_productos_a_comprar = input(f"Ingrese la cantidad de productos a comprar, {nombre_cliente}: ")

# Transforma la cantidad de productos a entero para que el range tome su valor, que no acepta string
cantidad_productos_a_comprar = int(cantidad_productos_a_comprar)

# Contadores que irán cambiando y serviran para mostrar el resultado final
total_con_descuentos = 0
total_sin_descuento = 0
resultado_completo_sin_descuento = 0 
# Recorrerá la cantidad de veces que el usuario haya ingresado de numero en la cantidad de producto 
for i in range(cantidad_productos_a_comprar):
    
    precio_producto = input("Ingrese el precio del producto: ")

    # Valida que el precio del producto sea digito, no se dijo nada que no podia ser 0, entonces se mantiene asi 
    while not precio_producto.isdigit():
        print("Error: debe ser un número entero.")
        precio_producto = input("Ingrese el precio del producto: ")

    # Transformando el precio del producto en int para poder hacer calculos con la variable
    precio_producto = int(precio_producto)
    
    # Defino cual es el porcentaje fijo, ya que es de 10% siempre
    PORCENTAJE = 10
    descuento = input("¿Tiene descuento? (s/n): ")
    # Para que solo puedan ingresar una opcion válida
    while descuento.lower() not in ["s", "n"]:
     descuento = input("¿Tiene descuento? (s/n): ")
        
    # El if verifica que sea s/S que se solicitaba
    if descuento == "s" or descuento == "S":
        # Calculo para sacar el porcentaje y el segundo, para obtener el valor del producto ya con el descuento de 10%
        descuento_sobre_producto = (precio_producto * PORCENTAJE) / 100    
        precio_producto_rebajado = precio_producto - (descuento_sobre_producto)
        total_con_descuentos += (precio_producto_rebajado)
        resultado_completo_sin_descuento += precio_producto
        
    # Para el caso que no tenga descuento en el producto     
    elif descuento == "n" or descuento == "N":
        total_sin_descuento += precio_producto
        resultado_completo_sin_descuento += precio_producto

resultado_final_con_descuentos = total_con_descuentos + total_sin_descuento
ahorro = resultado_completo_sin_descuento- resultado_final_con_descuentos
PROMEDIO = resultado_final_con_descuentos / cantidad_productos_a_comprar
print("........................")
print(f"Total sin descuentos: ${resultado_completo_sin_descuento}")
print("........................")
print(f"Total con descuentos: ${resultado_final_con_descuentos:.2f}")
print("........................")
print(f"Usted está ahorrando: ${ahorro:.2f}")
print("........................")
print(f"El precio promedio de compra es: ${PROMEDIO:.2f}")
print("........................")