while True:
    celular = int(input('Ingrese numero de celular'))
    if celular >= 10**8 and celular <10**9:
        print("bien")
        break
    else:
        print("mal")

while True:
    rut = int(input("Ingrese rut: "))
    if rut >99999999 or rut <5000000:
        print("bien")
        break
    else:
        print("mal")

print("FIN")