#este es un programa para calcular el costo de un viaje de 4 funciones.

#definir funciones
#Funcion 1: Conversion de dolares a pesos
def convertir_dolares_a_pesos(dolares):
    pesos = dolares * 19.4
    return pesos

#Funcion 2: Costo de hotel
def calcular_costo_hotel(hotel):
    noche = hotel * 185.0
    return noche

#Funcion 3: Costo del avion
def calcular_costo_avion(viaje):
    costo = viaje * 410.0 
    return costo

#Funcion 4:Costo de viaje en pesos
def costo_total_viaje(hotel, viaje):
    Ct = calcular_costo_hotel(hotel) + calcular_costo_avion(viaje)
    t = convertir_dolares_a_pesos(Ct)
    return t

#llamado de las funciones

opcion = int(input("Mete la opción del menú: "))
if opcion == 1:
    dolares = float(input())
    print(convertir_dolares_a_pesos(dolares))
elif opcion == 2:
    hotel = int(input())
    print(calcular_costo_hotel(hotel))
elif opcion == 3:
    viaje = int(input())
    print(calcular_costo_avion(viaje))
elif opcion == 4:
    hotel = int(input())
    viaje = int(input())
    print(costo_total_viaje(hotel, viaje))