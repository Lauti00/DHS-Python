def imprime(a, b="???"):
    print(a,b)

def devuelve():
    return 3,6

imprime("hola" , "!!!")
imprime(b="HOLA", a="!!")
imprime("Hola")


x=devuelve()
print(x)

x,y= devuelve()
print(x)
print(y)

#printf("%p  suma() /n") imprime la direccion de memoria de la funcion
#LAS TUPLAS SON INMUTABLES NO PUEDO MODIFICAR LOS VALORES EJ X= (4,5)