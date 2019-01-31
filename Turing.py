import ast
import os
from time import sleep
def Espacios(n):
	cadena = ""
	for i in range(n-1):
		cadena += " "
	return cadena

def Convertir(string):
	cadena = ""
	for i in string:
		cadena += str(i)
	return cadena

def ActualizaString(Cadena,Posicion,Pone):
	cont = 0
	String = []
	for i in Cadena:
		if cont == Posicion:
			String.append(Pone)
		else:
			String.append(i)
		cont+=1
	Cadena = ""
	Cadena = String
	return Cadena

def Obten_Delta(Tabla):
	Delta = []
	for i in range(len(Tabla)):
		Delta.append(Tabla[i].split(','))
	return Delta

def Obten_Estados(Tabla, Delta):
	Estados = []
	for i in range(len(Delta)):
		NewEstados = Delta[i]
		Estados.append(NewEstados[0])
	return Estados

def Busqueda(Estado_Actual,Lee,Delta):
	Lista = []
	for i in range(len(Delta)-1):
		New = Delta[i]
		if New[0] == Estado_Actual and Lee == New[2]:
			Lista.append(New[1])
			Lista.append(New[3])
			Lista.append(New[4])
	return Lista

def Computa(Estado_Actual, Tabla, Cadena, Posicion):
	Delta = Obten_Delta(Tabla)
	Estados = Obten_Estados(Tabla, Delta)
	NewEstado_Pone_Mov = []
	while Estado_Actual in Estados:
		Lee = Cadena[Posicion]
		NewEstado_Pone_Mov = Busqueda(Estado_Actual,Lee,Delta)
		Estado_Actual = NewEstado_Pone_Mov[0]
		Pone = NewEstado_Pone_Mov[1]
		Movimiento = NewEstado_Pone_Mov[2]
		os.system('cls')
		########################################################################
		print("		","================Maquina de Turing iniciada================","\n")		
		if Lee == "_":
			print("Lee:","Blanco")
		else:
			print("Lee:",Lee)
		print("Pone:",Pone)
		print("Estado Actual:",Estado_Actual)
		print("Movimiento:",Movimiento)
		print("		",Espacios(Posicion), Estado_Actual)
		print("		",Espacios(Posicion), "V")
		Cadena = ActualizaString(Cadena,Posicion,Pone)
		print("		",Convertir(Cadena))

		#input()
		sleep(1)		
		########################################################################

		if Movimiento == 'D\n':
			Posicion +=1
		elif Movimiento == 'I\n':
			Posicion -=1

		if Posicion >= len(Cadena)-19 or Posicion <= 18:
			print("		","================Maquina de Turing terminada================")
			break
	print("Estado de aceptacion:",Estado_Actual)



def main():
	#ARBIMOS EL ERCHIVO:
	nombre = str(input("Ingresa el nombre del archivo:"))
	Archivo = open(nombre, 'r')
	Contador  = 0
	Tabla = []
	# inicia bucle infinito para leer línea a línea
	while True: 
		Linea = Archivo.readline()  # lee línea
		Contador+=1
		if Contador > 2:
			Tabla.append(Linea)
		if not Linea: 
			break  # Si no hay más se rompe bucle
		#print(Linea)  # Muestra la línea leída
	Archivo.close()  # Cierra Archivo

	#INGRESAMOS LA CADENA PRUEBA:
	Cadena = str(input("Ingresa una cadena prueba: "))
	Cadena = "____________________"+Cadena+"____________________"
	#PREDEFINIMOS PARAMETROS
	Estado_Actual = 'q0'
	Posicion = 20

	#IMPRIMIMOS LOS MOVIMIENTOS DE LA MAQUINA DE TURING:
	Computa(Estado_Actual, Tabla, Cadena, Posicion)

if __name__ == '__main__':
  main()
