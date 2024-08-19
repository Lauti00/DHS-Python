def sumar(l) :
    r=0
    for e in l : #para cada elemento de la lista
        r+=e
    return r

def modificar(l):
    for i in range(len(l)):
        l[i]= l[i]+2
    return l

lista = [6,0,1,3]

r = sumar(lista) #estoy pasando por referencia 

nl= modificar(lista[:]) #GENERO UNA SUBLISTA DE LA ORIGINAL PARA NO PERDER LA PRIMERA QUE CREAMOS

