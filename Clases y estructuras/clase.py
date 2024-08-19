class Persona:
    def __init__(self, nombre,dni,edad):
        self.nombre = nombre
        self.dni=dni
        self.edad=edad


juan = Persona('juan' , '123456789' , 19)
pedro=Persona ('pedro', '987655432', 20)

personas =[juan,pedro]
for persona in personas:
    print(persona)  #imprimo el objeto direccion de memoria
