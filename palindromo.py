from datetime import datetime

def leer_pruebas(input):
	archivo = open(input,'r')
	pruebas = []
	for linea in archivo:
		linea= linea.strip()#se saca el salto de linea final
		pruebas.append(linea)
	return (pruebas)

def tildes_salto(s):
    reemplazo = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("\\n",""),
    )
    for a, b in reemplazo:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def limpiar_palabra(palabra):
    forbidden = {ord(c): None for c in ("?", "¿", "¡", "!", " ", ",", ".", ";", ":","-","[","]")}
    return palabra.lower().translate(forbidden)

#MAIN
def palindromo():
	output = open("output.txt",'w')
	output.write("Test Case ID | Resultado\n")
	pruebas = leer_pruebas('input.txt')
	cont = 1
	for test in pruebas:
		cid = cont
		output.write(str(cid)+" ")
		test = limpiar_palabra(tildes_salto(test)) 
		if(len(test) >1):
			inversa = test[::-1]
			if (test == inversa):
				output.write("si\n")
				cont+=1
			else:
				output.write("no\n")
				cont+=1
		else:
			output.write("no\n")
			cont+=1
	time = datetime.now()
	output.write("Prueba realizada: "+str(time))
	output.close()
palindromo()




