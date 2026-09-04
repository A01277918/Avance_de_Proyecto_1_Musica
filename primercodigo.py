
#esta funcion calcula el promedio de 3 variables 
def calcular_puntuacion(genero, ritmo, artista):
    promedio = (genero + ritmo + artista) / 3
    return promedio


genero = 5
ritmo = 4
artista = 5

puntuacion = calcular_puntuacion(genero, ritmo, artista)

print("La puntuación de la canción es:", puntuacion)