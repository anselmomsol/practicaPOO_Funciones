# Crear una función que pida al usuario el ancho y altura de un rectángulo y lo dibuje con caracteres producto (*):

def funcion_rectangulo(alto,largo):
    for a in range(alto):
            for l in range(largo):
                print("*", end="")
            print(" ")

#funcion_rectangulo(3,5)

def figura(alto,largo,figura):
        for a in range(alto):
            print(largo * figura, end="")
            print(" ")

#figura(3,5,"o") 

"""  Crear una función que pida un año y que escriba si es bisiesto o no. Se recuerda que
los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los
múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es
bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto. """

def bisiestos(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
	    print("Es bisiesto")
    else:
	    print("No es bisiesto")

#bisiestos(2010)

""" Crear una función que pida dos años y escriba cuántos años bisiestos hay entre esas
dos fechas (incluidos los dos años) """

def bisiestos2(anio, anio2):
    for anio in range(anio , anio2):
        if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
            print(anio, end=" ")

#bisiestos2(1800, 2000)

#Crear una función que pida cuántas listas se quieren crear y las solicite a continuación:
print(end = "\n")
def generar_lista():
    cant = int(input("Cuántas listas quiere generar? "))
    lista1 = []
    for i in range(cant):
        cant2 = int(input("Cuántas palabras tiene la lista? "))
        if cant2 > 0:
            for l in range(cant2):
                palabra = input("Digame la palabra ")
                lista1 += [palabra]
            print(lista1)
            lista1 = []

#generar_lista() 

""" Crear una función que recibe dos números y devuelve "mayor" (si el primer número es
mayor que el segundo), "menor", o "iguales" """

def mayor(num, num2):
    if num > num2:
        print(f"Mayor")
    elif num == num2:
        print("Iguales")
    else:
        print("Menor")

#mayor(1,2)
#mayor(2,1)
#mayor(1,1)

""" Hacer un programa que genere un número entero al azar (módulo random) entre 0 y
1000, y le vaya pidiendo al usuario que ingrese números enteros para adivinarlo. Si el
usuario ingresa un número menor que el objetivo, muestra "Es más alto!"; si el usuario
ingresa uno mayor, muestra "Es más bajo!"; si el usuario acierta, muestra "Viva
Python!", y termina. Si el usuario no acertó en 7 intentos, que muestre "Alpiste perdiste!
Booo" y termine.
"""
import random

def juego():
    numero_random = random.randint(0,1000)
    print(numero_random)

    condicion = True
    contador = 0

    while(condicion and contador < 7):
        num_resp = int(input("Ingrese un numero entre 0 y 1000: "))
        if num_resp < numero_random:
            print("El número es más alto!")
        elif num_resp > numero_random:
            print("El número es más bajo!")
        else:
            print("Viva Python!")
            condicion = False
        contador = contador + 1
    if condicion:
        print("Alpiste perdiste!")

#juego()

""" Crear una función que reciba un texto y devuelva el mismo texto pero con cada palabra
invertida. Por ejemplo, llamándola con "Esto es una prueba", debe devolver "otsE se
anu abeurp". """

def invertir(texto):
    cadena_invertida = ""
    for letra in texto:
        cadena_invertida = letra + cadena_invertida 
    return cadena_invertida

#print(invertir("Esto es una prueba"))


""" Crear una función que reciba dos palabras y que imprima linea por linea las primeras,
segundas, etc. letras de ambas palabras. Por ejemplo, llamándola con "Hola" y
"mundo", el resultado sería: """

def palabras(text, text2):
    if len(text) != len(text2):
        largo_total = max(len(text), len(text2))
        text = text.ljust(largo_total)
        text2 = text2.ljust(largo_total)
        
    for a, j in zip(text,text2):
        print(a,j)
    return

#palabras("Hola","Mundo")

""" Crear una función que reciba una tupla y devuelva si la tupla está ordenada (de menor a
mayor) o no. """

def tupla_ordenada(tupla):
    tupla_ord = list(tupla)
    tupla_ord.sort()

    if tupla == tupla_ord:
        print("La tupla esta ordenada de mayor a menor")
    else:
        print("La tupla NO esta ordenada de mayor a menor")


#tupla_ordenada([1,3,4,5,6])
#tupla_ordenada([5,4,3,2,1])

""" Crear dos funciones que permitan convertir de segundos a horas, minutos y segundos,
correspondientemente. """

def horas_min_seg(segs):
    mins, seg = divmod(segs, 60)
    hrs, mins = divmod(mins, 60)
    print(f"{hrs}hs {mins}min {seg}seg")
    

def segundos(hrs, mins, segs):
    seg = hrs * 3600 + mins * 60 + segs
    print(f"{seg}seg")
    
    
#horas_min_seg(10000)
#segundos(10, 40, 35)

""" Crear una función que pida al usuario 3 números y devuelva cuál es el mayor, cuál es el
menor y cuál es la media de los 3 números. """

def comparar_numeros():
    lista_num = []
    for i in range(3):
        num = int(input("Ingrese un número: "))
        lista_num.append(num)
    print(min(lista_num))
    print(max(lista_num))
    print(sum(lista_num)/len(lista_num))
    
    
#comparar_numeros()

""" Escribir una función que tome una lista de palabras y devuelva cuál es la más larga y
cuántos caracteres tiene. """

def palabras(*palabras):
    cant_letras = 0
    pal_mas_larga = ""
    for palabra in palabras:
        cant_carac = len(palabra)
        if cant_carac > cant_letras:
            cant_letras = cant_carac
            pal_mas_larga = palabra
    print(f"La palabra más larga de la lista es {pal_mas_larga} y tiene {cant_letras} letras")
    
    
#palabras("Hola", "Mundo", "Python", "Funciones")