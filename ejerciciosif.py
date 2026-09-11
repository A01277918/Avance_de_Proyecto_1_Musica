#¿Es un triángulo? Si los valores de dichas cantidades pueden corresponder a las longitudes de los lados de un triángulo.

print ("Este es un código para determinar si tres valores pueden formar un triángulo.")
a = float(input("Ingrese el valor del primer lado: "))
b = float(input("Ingrese el valor del segundo lado: "))
c = float(input("Ingrese el valor del tercer lado: "))

if a + b > c and a + c > b and b + c > a:
    print("Los valores ingresados pueden formar un triángulo.")

#¿Es escaleno? En el caso de que las medidas puedan corresponder a las longitudes
#de los lados de un triángulo, si dicho triángulo es escaleno.

print ("Este es un código para determinar si la medidas de los lados de un triangulo son escaleno")
d = float(input("Ingrese el valor del primer lado: "))
e = float(input("Ingrese el valor del segundo lado: "))
f = float(input("Ingrese el valor del tercer lado: "))

if d != e and e != f and d != f:
    print("Entonces los valores dados hacen que se pueda formar un triángulo escaleno")

#¿Es equilátero? En el caso de que las medidas puedan corresponder a 
#las longitudes de los lados de un triángulo, si dicho triángulo es equilátero.

print ("Este es un código para determinar si los lados de un triangulo son equiláteros")

g = float(input("Ingrese el valor del primer lado: "))
h = float(input("Ingrese el valor del segundo lado: "))
i = float(input("Ingrese el valor del tercer lado: "))
if g == h and h == i and g == i:
    print("Entonces los valores dados hacen que este sea un triangulo equilátero")
else:
    print("Los valores dados no forman un triangulo equilátero")

#¿Es isósceles? En el caso de que las medidas puedan corresponder
#a las longitudes de los lados de un triángulo, si dicho triángulo es isósceles.

print ("Este es un código para determinar si los lados de un triangulo son isosceles")

j = float(input("Ingrese el valor del primer lado: "))
k = float(input("Ingrese el valor del segundo lado: "))
l = float(input("Ingrese el valor del tercer lado: "))
if j == k or k == l or j == l:
    print("Entonces los valores dados hacen que este sea un triangulo isósceles")


#Determinar si un año es bisiesto. Un año es bisiesto si es múltiplo
#  de 4 (por ejemplo, 1984). Sin embargo, los años múltiplos de 100
#  sólo son bisiestos cuando a la vez son múltiplos de 400 (por
#  ejemplo, 1800 no es bisiesto, mientras que 2000 si lo es).

print("Este es un código para determinar si un año es bisiesto o no")


año = int(input("Ingrese el año que desea saber i es bisiesto o no"))

if año % 4 == 0 and (año % 100 == 0 and año % 400 == 0):
        print("El año es bisiesto.")