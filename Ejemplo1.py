from math import pi
#CALCULAR EL VOLUMEN DE UNA ESFERA#

cadena_leida=input("Dame el radio \n")

radio= float(cadena_leida)

volumen= 4/3 * pi * radio **3
print("El volumen es:" , volumen , "metros cubicos") #la , va a permitir separar la cadena
print("Volumen " + str(volumen) + "metros cubicos") #Va a concatenar
print("Volumen  {0:.4f} metros cubicos".format(volumen)) #Uso formato

s="-"
print(s*50)
print("CONDICIONALES")
a=float((input("Ingrese el valor de a \n")))

if a>=0 :
    print("El valor de a es mayor a cero")
else:
    print("EL valor es menor a cero")