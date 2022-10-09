nombres = []
materias = []
 
print ("Ingrese el nombre y cantidad de alumnos de la materia")
 
while True:
    nombres.append(input("Nombre: "))
    materias.append(int(input("No. Alumnos: ")))
    if input("¿Desea continuar? S/N") == "N": break 
 
print ("Nombres de materias con alumnos: ")
for i, nalumno in enumerate(materias):
    if nalumno > 0:
        print ("Materia:",nombres[i],"  No. Alumnos: ", nalumno)