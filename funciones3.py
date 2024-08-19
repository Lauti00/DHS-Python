def devuelve(y):
    global z
    z= y*3
    # z=y*3  #NOTAR: cuando hago una nueva asignacion dentro de una funcion estamos creando una variable local

    r=x+y+z 

x=10
z=2

r=devuelve(5)
print(r)
#desde la funcion hacia afuera yo puedo nombrar las variables globales


#SI QUIERO MODIFICAR LA VARIABLE Z Y QUE QUEDE COMO VARIABLE GLOBAL USAMOS EL GLOBAL
#LAs variables globales siempre son de lectura , en python necesito aclarar que quiero usar la variable global y no la local.
