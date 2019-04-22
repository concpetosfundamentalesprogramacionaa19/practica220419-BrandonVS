"""
	Problema 1 en python
	autor @BrandonVS
"""
# Se ingresan el numero de horas y el costo por horas
print ("Ingrese el numero de horas trabajadas: ")
horas = input()

print ("Ingrese el costo por hora: ")
costo = input()

# Se calcula el pago multiplicando horas y costo
paga = float(horas) * float(costo)

# Se calcula el descuento del seguro social dividiento el pago mensual para 10
descuento = (float(paga)/10)

# Se imprime el numero de horas, el costo por horas, el sueldo mensual y el descuento del seguro social
print ("Por trabajar %s horas, usted recibira: %s dolares este mes.\nEl descuento de seguro social será de: %.2f dolares." % (horas, paga, descuento))