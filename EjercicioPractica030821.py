#EJERCICIO 4
#Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la primera letra de cada palabra a mayúscula 
#y las demás letras a minúscula, dejando inalterados los demás caracteres. Precondición: el separador de palabras es el espacio: " ".
import string

def title(titulo:str):
    t=titulo
    return string.capwords(t, None)

#main code
tit = input("Por favor, ingrese la cadena que desea: ")
print("resultadosss: ",title(tit))
print("Quedemosnos unicamente con un mensaje final feliz: Hola Universo!")


