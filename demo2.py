"""
	Ejemplo de lenguaje python
	autor @BrandonVS
"""

import sys

# Se declaran las variables
dato1 = sys.argv[1]
dato2 = sys.argv[2]

# Realizamos la suma y multiplicacion
suma = int(dato1) + int(dato2)
multipl = int(dato1) * int(dato2)

# Imprimimos los resultados
print ("La suma es: %s" % suma)
print ("La multiplicacion es: %s" % multipl)