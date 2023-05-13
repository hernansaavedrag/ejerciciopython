def registrar_cliente():
    print("Registro de Cliente")
    rut = input("Rut (sin dígito verificador ni puntos): ")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    comuna = input("Comuna: ")
    correo = input("Correo: ")
    edad = int(input("Edad: "))
    celular = input("Celular: ")
    tipo = input("Tipo: Preferencial/Habitual/Ocasional: ")
    print("Cliente registrado con éxito\n")

def registro_de_pedido():
    print("Registro de Pedido")
    print("Opción 1:")
    # ... lógica para la opción 1
    print()
    print("Opción 2:")
    # ... lógica para la opción 2
    print()
    print("Opción 3:")
    # ... lógica para la opción 3
    print()

    monto = float(input("Ingrese el monto a cancelar: "))
    efectivo = float(input("Ingrese el monto entregado por el cliente: "))

    if efectivo > monto:
        vuelto = efectivo - monto
        print("Vuelto:", vuelto)
    elif efectivo == monto:
        print("No tiene vuelto")
    else:
        print("Dinero insuficiente")

    print()


opcion = 0
while opcion != 4:
    print("Sushi-Nikkey App")
    print("1. Registrar Cliente")
    print("2. Consultar Datos Cliente")
    print("3. Registro de Pedido")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        registrar_cliente()
    elif opcion == 2:
        consultar_datos_cliente()
    elif opcion == 3:
        registro_de_pedido()
    elif opcion == 4:
        print("Gracias por preferir Sushi-Nikkey")
    else:
        print("Opción inválida")
    print()


import re

def validar_rut(rut):
    # Validación de formato y rango del Rut
    if not re.match(r'^\d{7,8}$', rut):
        return False

    rut_numeros = int(rut)
    if rut_numeros < 5000000 or rut_numeros > 99999999:
        return False

    return True

def validar_numero(numero):
    # Validación de longitud del número
    if isinstance(numero, int) and 10**8 <= numero < 10**9:
        return True
    return False
'''
En este ejemplo, la función validar_numero verifica si el número es un entero (isinstance(numero, int)) 
y si está en el rango de 10**8 (100,000,000) 
inclusive hasta 10**9 (1,000,000,000) no inclusive. 
De esta manera, se asegura de que el número tenga exactamente 9 dígitos.
'''
