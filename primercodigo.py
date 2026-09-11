
# --------------------------------
# FUNCION PARA OBTENER ESTADISTICAS
# --------------------------------

def obtener_estadisticas():
    puntos = int(input("Puntos: "))
    asistencias = int(input("Asistencias: "))
    rebotes = int(input("Rebotes: "))
    robos = int(input("Robos: "))
    pases_fallidos = int(input("Pases fallidos: "))
    puntos_tres = int(input("Puntos de 3: "))
    perdidas = int(input("Perdidas de balon: "))

    return puntos, asistencias, rebotes, robos, pases_fallidos, puntos_tres, perdidas


# --------------------------------
# FUNCION PARA CALCULAR DESEMPENO
# --------------------------------

def calcular_desempeno(puntos, asistencias, rebotes, robos, pases_fallidos, puntos_tres, perdidas):

    puntuacion = (puntos + asistencias + rebotes + robos + puntos_tres - pases_fallidos - perdidas)

    return puntuacion


# --------------------------------
# FUNCION PARA OBTENER CALIFICACION
# --------------------------------

def obtener_calificacion(puntuacion):

    if puntuacion >= 30:
        calificacion = 10
    elif puntuacion >= 20:
        calificacion = 8
    elif puntuacion >= 10:
        calificacion = 6
    else:
        calificacion = 4

    return calificacion


# --------------------------------
# FUNCION PARA MOSTRAR RESULTADO
# --------------------------------

def mostrar_resultado(nombre, puntuacion, calificacion):

    print()
    print("Jugador:", nombre)
    print("Puntuacion:", puntuacion)
    print("Calificacion:", calificacion, "/ 10")


# --------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------

print("ESTADISTICAS DE BASQUETBOL")
print("---------------------------")

nombre = input("Nombre del jugador: ")

estadisticas = obtener_estadisticas()

puntuacion = calcular_desempeno(*estadisticas)

calificacion = obtener_calificacion(puntuacion)

mostrar_resultado(nombre, puntuacion, calificacion)