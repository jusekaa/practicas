#Ejercicio definir una funcion que permita imprimir la tabla de multiplicar, 
# pero esta función debe recibir la tabla que va a operar y el operador es decir 
# que la función que realicen va a ejecutar cualquier operación.
import operator

def imprimir_tabla(tabla,operador,simbolo):
    for i in range (1,12+1):
        resultado= operador(tabla,i)
        print(f"{tabla} {simbolo} {i} = {resultado}")
numero = int(input("Indiqueme un número para la tabla: "))
print("Selecciona la operación que deseas realizar:")
print("1) Multiplicación")
print("2) Suma")
print("3) Resta")
print("4) División")

while numero:
    opcion = input("Introduce el número de la operación (1-2-3-4): ")
    
    if opcion in ['1', '2', '3', '4']:
        break
    else:
        print("Opción no válida. Por favor introduzca 1, 2, 3 o 4")
if opcion == '1':
    imprimir_tabla(numero, operator.mul, '*')
elif opcion == '2':
    imprimir_tabla(numero, operator.add, '+')
elif opcion == '3':
    imprimir_tabla(numero, operator.sub, '-')
elif opcion == '4':
    imprimir_tabla(numero, operator.truediv, '/')
else:
    print("Opción no válida. Por favor introduzca 1,2,3 o 4 ")
    
    
    """
    #Crear un sistema en el cual pueda saber quien aprobó la materia según la calificación
numero_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
estudiantes = []
calificacion_minima = 3.0

for i in range(numero_estudiantes):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    
    while True:
        calificacion = float(input(f"Ingrese la calificación de {nombre}: "))

        if 0 < calificacion < 5:
            estudiantes.append({"Nombre": nombre, "Calificacion": calificacion})
            break
        else:
            print(f"Calificación inválida para {nombre} Debe estar entre 0 y 5, digite nuevamente ")

for estudiante in estudiantes:
    if estudiante["Calificacion"] >= calificacion_minima:
        print(f"{estudiante['Nombre']} aprobó con una calificación de {estudiante['Calificacion']}")
    else:
        print(f"{estudiante['Nombre']} no aprobó, su calificación fue de {estudiante['Calificacion']}")
    
    
    
    
    
    """