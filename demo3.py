"""
	Ejemplo de lenguaje python
	autor @BrandonVS
"""

# Pedimos que se ingresen los valores
print ("Ingrese el valor 1: ")
valor1 = input () 

print ("Ingrese el valor 2: ")
valor2 = input ()

# Realizamos la suma y la multiplicacion
suma = int(valor1) + int(valor2)
mult = int(valor1) * int(valor2)

# Imprimimos el valor de la suma y la multiplicacion
print ("La suma es: %d\nLa multiplicacion es: %d" % (suma, mult))