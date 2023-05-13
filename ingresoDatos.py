op = True

nombre = input("Ingrese su nombre: ")
rut = input("Ingrese su rut con puntos y guión: ")
while op == True:
    try:
        montoCredito = int(input("Ingrese monto a solicitar: "))
        if montoCredito > 500000 :
            cuotas= int(input("Ingrese cuotas para pagar: "))
            if cuotas >= 3 and cuotas <= 84:
                edad = int(input("Ingrese su edad: "))
                if edad >= 24 and edad <=79 :
                    nacion = input("Ingrese Nacionalidad: ").upper() #mayúscula
                    nacionalidad = nacion.lower() #minúscula
                    if nacionalidad == "chilena" or nacionalidad == "chileno":
                        sueldo = int(input("Ingrese su sueldo: "))
                        if sueldo >= 250000:
                            aLaboral = int(input("Ingrese antigüedad laboral: "))
                            if aLaboral >= 3 :
                                deuda = input("Tiene deuda (s/n): ")
                                deuda2 = deuda.lower()
                                if deuda2 == "n":
                                    print("Aceptado") #aqui comienza los calculos.
                                    op = False
                                else:
                                    print("UD no debe tener deuda, no aceptado!! ")
                            else:
                                print("No aceptado, ud debe tener una antigüedad de 3 años")
                        else:
                            print("Su sueldo debe ser mayor a $ 250.000")
                    else:
                        print("UD debe ser Chileno")                
                else:
                    print("No cumple, la edad debe estar entre 24 y 79")                    
            else:
                print("No cumple, las cuotas debe ser entre 3 y 84")
        else:
            print("No cumple con el monto a solicitar, debe ser mayor a $500.000 ")
    except :
        print("Error de valor")
                