def dividir():
    try:
        
        num1 = float(input("Ingrese el número 1: "))
        num2 = float(input("Ingrese el número 2: "))
        
        
        resultado = num1 / num2
        
    except ZeroDivisionError:
        return "No se puede dividir por cero."
    except ValueError:
        return "Cantidad inválida. Por favor ingrese números válidos."
    except Exception as e:
        return f"Ha ocurrido un error: {e}"

    return resultado

print(dividir())
def promedio():
    opcion = int(input("Pulse 1 para calcular el promedio \n"))
    suma = 0
    if opcion == 1:
        cantidad = int(input("Ingrese la cantidad de números \n"))
        
        for _ in range(cantidad):
            numero = float(input("Ingrese el número \n"))
            suma += numero

        if cantidad > 0:
            promedio = suma / cantidad
            print("El promedio es:", promedio)
        else:
            print("La cantidad de números debe ser mayor que 0.")
    else:
        print("Opción no válida.")

promedio()


