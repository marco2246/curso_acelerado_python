'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio8.py
Autor: Marco Vazquez
Action: detecta numero negativos
'''
numero = int(input("Escriba un número positivo: "))
if numero < 0:
  print("Numero negativo")
elif numero == 0:
  print("Numero neutro")
else:
  print("Numero positivo")
