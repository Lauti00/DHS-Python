s='-'
l=[1,2,3]
t=l
l[1]=1111

t= l[:] #OPERADOR DE CORTE ME GENERA UNA COPIA, GENERA SUBLISTA
print(s*60)
print("Operador Corte")
print(s*60)
print ("LA lista b es:" ,t)
t[1]=2222 #ME CAMBIA EL VALOR DE T PERO NO EL DE L POR LA SUBLISTA QUE CREAMOS CON EL OPERADOR DE CORTE

print(s*60)
print("Listas de 1")
unos= [1]*8 #Lista de 8 unos
print(unos)

print(s*60)
print("Generador de lista en un rango")
escalera = list(range(1,11)) #Lista del 1 al 10
print(escalera)



print(s*60)
print("EJEMPLO 2")
print(s*60)

x=[1,2,3]
y=x
w=x[:]

print("¿La lista x es igual a la y? \n" , x==y) #COMPARO LAS LISTAS
