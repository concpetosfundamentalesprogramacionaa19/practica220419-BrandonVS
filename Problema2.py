"""
	Problema 1 en python
	autor @BrandonVS
"""
# Se piden las variables x, y ,z
x = input("Ingrese el valor de x: ")
y = input("Ingrese el valor de y: ")
z = input("Ingrese el valor de z: ")

# Se calcula m con la formula descrita en el problema
m = (float(x)+(float(y)/float(z)))/(float(x)-(float(y)/float(z)))

# Se imprime el valor de m, junto con las variables x, y, z
print("El valor de m en base a las variables:\nx = %s\n\ty = %s\n\t\tz = %s\nDa como resultado: \n\t\t\tm = %.2f" % (x, y ,z ,m))