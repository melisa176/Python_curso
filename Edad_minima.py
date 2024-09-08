edad=int(input("Ingrese su edad"))
if(edad>=0):
    if(edad<18):
        print("Usted es menor de edad")
    elif(edad>=18 and edad<65):
        print("Usted es adulto")
    else:
        print("Usted es adulto mayor")
else:
    print("Edad fuera de rango")