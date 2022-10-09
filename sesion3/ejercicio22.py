sorteo = []
 
print ("Ingrese el número del sorteo")
 
while True:
    sorteo.append(int(input("No. Sorteo: ")))
    if input("¿Desea continuar? S/N") == "N": break 
 
sorteo.sort()
print("Números ordenados de menor a mayor: ",sorteo)