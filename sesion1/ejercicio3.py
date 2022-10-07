'''
*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio3.py
Autor: Programador x
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
hextra = float(input("Introduce horas extra: "))
paga1 = coste * hextra
paga = horas * coste
pagat = paga1 + paga
print("Tu paga es", pagat)