class Cliente:
    def __init__(self, rut, nombre, direccion, comuna, correo, edad, celular, tipo):
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.comuna = comuna
        self.correo = correo
        self.edad = edad
        self.celular = celular
        self.tipo = tipo


clientes = []


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
    cliente = Cliente(rut, nombre, direccion, comuna, correo, edad, celular, tipo)
    clientes.append(cliente)
    print("Cliente registrado con éxito\n")


def consultar_datos_cliente():
    print("Consultar Datos Cliente")
    rut = input("Ingrese el Rut del cliente a consultar: ")
    for cliente in clientes:
        if cliente.rut == rut:
            print("Rut:", cliente.rut)
            print("Nombre:", cliente.nombre)
            print("Dirección:", cliente.direccion)
            print("Comuna:", cliente.comuna)
            print("Correo:", cliente.correo)
            print("Edad:", cliente.edad)
            print("Celular:", cliente.celular)
            print("Tipo:", cliente.tipo)
            print()
            return
    print("Cliente no encontrado\n")


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
