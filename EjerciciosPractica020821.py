#EJERCICIO 1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura>
# es cada una de las asignaturas de la lista

print("\n**********ASIGNATURAS Y MAT*********** \n")
asignaturas = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lengua']

for i in asignaturas:
    print ("Yo estudio ",i)

#EJERCICIO 2
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras
# que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
print("\n**********ABECEDARIO*********** \n")
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o' ]

for i in abecedario:
    if abecedario.index(i) % 3:
        abecedario.remove(i)

print("Hola Mundo")

#EJERCICIO 3
#Escribir un programa que almacene en una lista los siguientes precios:50, 75, 46, 22, 80, 65, 8
#  y muestre por pantalla el menor y el mayor de los precios.

print("\n**********PRECIOS*********** \n")
precios = [50, 75, 46, 22, 80, 65, 8]

precios.sort()

print("Los precios de manera ascendente son: ", precios)


#EJERCICIO 4
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales
# o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus
# ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

print("\n**********MODULO DE INFORMACION TRIBUTARIA*********** \n")
print("\nBienvenido, este es el mdoulo de información tributaria \n")

edad = input("Por favor, ingresa tu edad: ")
ing_men = input("Ahora sus ingresos mensuales porfi: ")

edad = int(edad)
ing_men = int(ing_men)

if edad >= 16 and ing_men >= 1000:
    print("Lo sentimos, es usted un adulto COMPLETAMENTE funcional y debe pagar impuestos")