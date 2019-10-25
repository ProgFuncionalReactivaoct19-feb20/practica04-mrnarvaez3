"""
	# practica04
	## En función del archivo .txt, hacer:
	- Encontrar todos los que han hecho mas de 3 goles
	- Encontrar los que son del país Nigeria
	- El valor mínimo y máximo de la caracteristica Height
	Roberto N

"""
#	para importar archivo txt
import codecs
import json

archivo = codecs.open("datos.txt", "r")

lineas = archivo.readlines()

lineas_diccionario = []
lineas_diccionario = [json.loads(l) for l in lineas]

funcion1 = (lambda x: list(x.items())[1][1]>=3)

funcion2 = (lambda x: list(x.items())[0][1] == "Nigeria")

#  Lista para obtener todas las estaturas
lista = list(map(lambda x: list(x.items())[2][1], lineas_diccionario))
#  obtengo maximo y minimo de la lista
minimo = min(lista)
maximo = max(lista)
#  obtenemos el diccionario de los minimos y maximos
funcion3 = list(filter(lambda x: list(x.items())[2][1] == minimo, lineas_diccionario))
funcion4 = list(filter(lambda x: list(x.items())[2][1] == maximo, lineas_diccionario))


#  imprimiendo datos de los que cumplen la condicion
print("Jugadores con mas de 3 goles:\n", list(filter(funcion1, lineas_diccionario)))
print("Jugadores Nigerianos: \n", list(filter(funcion2, lineas_diccionario)))

print("Jugador con menos estatura: \n",funcion3)
print("Jugador con mas estatura: \n", funcion4)
