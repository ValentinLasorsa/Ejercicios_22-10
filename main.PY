import os
import random
#Funciones
def listaMenorAMayor(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                aux=lista[j]
                lista[j] = lista[j + 1]
                lista[j+1]=aux
    print(lista)
    return lista
def listaMayorAMenor(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1):
            if lista[j] < lista[j + 1]:
                aux=lista[j]
                lista[j] = lista[j + 1]
                lista[j+1]=aux
    print(lista)
    return lista
# Inicio programa
#Ej 1
print("Ejercicio 1")
sueldos=[]
for j in range(1,16):
    sueldo=int(input(f"Ingrese el sueldo del {j} empleado "))
    sueldos.append(sueldo)
listaMenorAMayor(sueldos)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#Ej 2
print("Ejercicio 2")
sueldos=[]
for j in range(1,16):
    sueldo=int(input(f"Ingrese el sueldo del {j} empleado "))
    sueldos.append(sueldo)
listaMayorAMenor(sueldos)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#Ej 3
print("Ejercicio 3")
listaNumeros=[]
listaPositivos=[]
listaNegativos=[]
for j in range(1,21):
    numero=int(input(f"Ingrese el {j} número "))
    listaNumeros.append(numero)
    if numero>0:
        listaPositivos.append(numero)
    else:
        listaNegativos.append(numero)
listaMenorAMayor(listaPositivos)
listaMayorAMenor(listaNegativos)
print("La lista original quedó así:",listaNumeros,"- La lista positiva así:",listaPositivos,"- Y La negativa así:",listaNegativos)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#Ej 4
print("Ejercicio 4")
numerosRandoms=[]
for j in range(25):
    numeroRandom=random.randint(1,50)
    numerosRandoms.append(numeroRandom)
print("La lista original quedó así:",numerosRandoms)
listaMayorAMenor(numerosRandoms)
print("La lista decreciente quedaría así:",numerosRandoms)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#Ej 5
print("Ejercicio 5")
listaProductos=[]
productoRepetido=[]
for j in range(1,16):
    producto=int(input(f"Ingrese el {j} producto "))
    listaProductos.append(producto)
for j in range(5):
    aux=0
    productoRandom=random.randint(0,14)
    while productoRandom in productoRepetido:
        productoRandom=random.randint(0,14)
    productoRepetido.append(productoRandom)
    aux=listaProductos[productoRandom]
    print("El producto con precio $"+str(aux)+" será aumentado")
    listaProductos[productoRandom]=aux+((aux*15)/100)
print("La nueva lista con los aumentos queda así:")
listaMenorAMayor(listaProductos)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#Ej 6
print("Ejercicio 6")
sueldos=[]
sueldosAumentados=[]
for j in range(1,16):
    sueldo=int(input(f"Ingrese el sueldo del {j} empleado "))
    sueldos.append(sueldo)
for h in sueldos:
    h=h+((h*20)/100)
    sueldosAumentados.append(h)
listaMayorAMenor(sueldosAumentados)
print("Los sueldos originales:",sueldos, "- La lista de sueldos con el 20% extra:",sueldosAumentados)
input("\033[1mPresione enter para salir\033[0m")
os.system('cls')
