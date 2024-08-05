s='-'
print(s*60)
print("UTILIZANDO WHILE...")
print(s*60)
a=0

while a<=3:
    print("EL valor de a es:" , a)
    a=a+1
    

print(s*60)

print("UTILIZANDO FOR....")
print(s*60)

print("Para cada 'a' que pertenece a la lista, tenemos: ")
for a in [3,4.25,"Hola",True]: #para cada a que pertenece a la lista 
    print (a)

print(s*60)

print("OTRA FORMA DE UTILIZAR EL FOR")
print(s*60)

for a in range (0,5):  #Generador de numeros va a comenzar en 0 y termina en 5
    print ("EL valor de a es:" , a)
print(s*60)
for a in range (5): #Inicializa en 0 directamente hasta 4
    print("El valor de a es: ", a)
print(s*60)
for a in range (-1,5,2): #Va a ir de -1 a 5 de dos en dos
    print("El valor de a es: " , a)    
print(s*60)