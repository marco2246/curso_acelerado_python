'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio17.py
Autor: Marco Vazquez
Action: Tablas de multiplicar
'''
valor = int(input("Ingrese número entre el 1 y el 10: "))
if  valor > 0 and valor < 13:
  for f in range(1,13):
	  multiplicacion = valor * f #hacemos la multiplicación
	  print(f'{valor} x {f} = {multiplicacion}') #mostramos el resultado
else:
  print("Valor incorrecto")