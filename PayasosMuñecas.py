print("Sistema de Ventas de Juguetes")

while True:
    try:
        print("Opciones de Juguetes")
        print("********************")
        print("1. Payasos")
        print("2. Muñecas")
        print("3. Salir")
        op = int(input("Ingrese Opción: "))
        
        if op == 1:
            payasos = int(input("Ingrese cantidad de Payasos: "))
            pesoPayasos = payasos * 300
            print("1. Zona norte")
            print("2. Zona centro")
            print("3. Zona sur")
            zona = int(input("Ingrese Zona: "))
            if zona == 1:
                if pesoPayasos < 1000:
                    envio = 3000
                else:
                    envio = 5000
            else:
                if zona == 2 :
                    if pesoPayasos < 1000:
                        envio = 2000
                    else:
                        envio = 3000
                else:
                    if zona == 3:
                        if pesoPayasos < 1000:
                            envio = 4000
                        else:
                            envio = 7000
            print("El peso total de payasos  es: ",pesoPayasos,"gr.")
            print("EL total a pagar es : $",envio)
            
        else:
            if op == 2:
                muñecas = int(input("Ingrese cantidad de Muñecas: "))
                pesoMuñecas = muñecas * 450
                print("1. Zona norte")
                print("2. Zona centro")
                print("3. Zona sur")
                zona = int(input("Ingrese Zona: "))
                if zona == 1:
                    if pesoMuñecas < 1000:
                        envio = 3000
                    else:
                        envio = 5000
                else:
                    if zona == 2 :
                        if pesoMuñecas < 1000:
                            envio = 2000
                        else:
                            envio = 3000
                    else:
                        if zona == 3:
                            if pesoMuñecas < 1000:
                                envio = 4000
                            else:
                                envio = 7000
                print("El peso total de Muñecas  es: ",pesoMuñecas,"gr.")
                print("EL total a pagar es : $",envio)

            else:
                if op == 3:
                    break 
    except :
        print("Debe ingresar un valor válido")
    