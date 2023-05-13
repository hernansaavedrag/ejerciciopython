opcion = 0
rut=""
pedido = 0
california = 5100
ahumado = 6100
tempura = 5800
total = 0

while opcion != 4:
    print("Sushi-Nikkey App")
    print("1. Registrar Cliente")
    print("2. Consultar Cliente")
    print("3. Registro Pedido")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print("Registro Cliente")
        #aca comenzamos la validación de rut ******
        while True:
            rut = int(input("Ingrese su rut: "))
            if rut >5000000 and rut < 99999999:
                #print("bien")
                break
            else:
                print("Rut mal ingresado, ingrese nuevamente")
        # ****** fin validacion de rut

        nombre = input("Ingres su nombre: ")
        direccion = input("Ingrese su dirección: ")
        comuna = input("Ingrese su comuna: ")

        while True:
            correo = input("Ingrese su correo: ")
            if "@" in correo:
                break
            else:
                print("Correo mal ingresado, ingrese nuevamente")
        
        while True:
            edad = int(input("Ingrese su edad: "))
            if edad >= 18 :
                break
            else:
                print("edad mal ingresada, edad debe ser mayor o igual a 18")
        while True:
            try:
                celular = int(input("Ingrese su número de celular: "))
                if celular >= 10**8 and celular < 10**9:
                    break
                else:
                    print("Celular mal ingresado, ingrese nuevamente")
            except ValueError:
                print("Ud ingreso una palabra")
        tipo = input("Tipo: Preferencial/Habitual/Ocasional: ").lower()
        #if tipo =="preferencial" or tipo == "habitual" or tipo =="ocasional":
        print("")
        print("Cliente ingresado con éxito\n")
    else:
        
        if opcion == 2:
            if rut != "":
                print("Datos del cliente")
                print("*****************")
                print("Rut: \t\t", rut)
                print("Nombre: \t",nombre)
                print("Dirección: \t",direccion)
                print("Comuna: \t",comuna)
                print("Correo: \t",correo)
                print("Edad: \t\t",edad )
                print("Celular: \t",celular)
                print("Tipo: \t",tipo)
            else:
                print("No hay datos que mostrar\n")
        else:
            if opcion == 3: 
                while pedido != 4:
                    print("Registro de Pedido")
                    print("1. Opción 1 (California - $ 5.100)")
                    print("2. Opción 2 (Crab Ahumado - $ 6.100)")
                    print("3. Opción 3 (Tempura Tina Nikkei - $ 5.800)")
                    print("4. Salir")
                    pedido = int(input("Ingrese su opción: "))
                    if pedido == 1 :
                        cant = int(input("Ingrese cantidad: "))
                        precioCalifornia = cant * california
                        total = total + precioCalifornia
                    else:
                        if pedido == 2:
                            cant = int(input("Ingrese cantidad: "))
                            precioAhumado = cant * ahumado
                            total = total + precioAhumado
                        else:
                            if pedido == 3 :
                                cant = int(input("Ingrese cantidad: "))
                                precioTempura = cant * tempura
                                total = total + precioTempura
                print("El total a pagar es:  ",total)
                efectivo = int(input("Ingrese el monto entregado por el cliente"))
                if efectivo > total:
                    vuelto = efectivo - total
                    print("Vuelto: ",vuelto)
                else:
                    if efectivo == total:
                        print("No tiene vuelto")
                    else:
                        print("Dinero insuficiente")
                        

            else:
                print("Gracias por preferir Sudhi - Nikkey")






        







