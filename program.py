#laboratorio 3, 
#4.a.- Programas que involucran estructuras de decisión

#1. Declarar funciones

#Funcion 1
def valida (num):
    if num > 0:
        return True
    else:
        return False

#Funcion 2
def corriente (voltaje, resistencia):
    if resistencia <= 0:
        #indicar que la operacion no fue exitosa
        return -1
    else:
        corriente = voltaje / resistencia
        return corriente

#Funcion 3

def voltaje (corriente, resistencia):
    voltaje = corriente * resistencia
    return voltaje

#Funcion 4

def resistencia (corriente, voltaje):
    if corriente <= 0:
        #indicar que la operacion no fue exitosa
        return -1
    else:
        resistencia = voltaje / corriente
        return resistencia

#2. LLamado de las funciones

opcion = int(input())
if (opcion == 1):
    num = float(input())
    print(valida(num))
elif (opcion == 2):
    voltaje = float(input())
    resistencia = float(input())
    print(corriente(voltaje, resistencia))
elif (opcion == 3):
    corriente = float(input())
    resistencia = float(input())
    print(voltaje(corriente, resistencia))
elif (opcion == 4):
    corriente = float(input())
    voltaje = float(input())
    print(resistencia(corriente, voltaje))
else:
    print("entrada no valida")
