#Karla Ivonne Serrano Arevalo
#Ejerercicio 1
#22 noviembre 2016

peso=float(input("Tu peso en Kg: "))
estatura=float(input("Tu estatura en Cm: "))

imc=peso/(estatura*estatura)


if imc<16:
	print "Delgadez severa"

elif imc>16 and imc<16.99:
	print "Delgadez moderada"

elif imc>17 and imc<18.49:
	print "Delgadez leve"

elif imc>25 and imc<30:
	print "Sobrepeso"

elif imc>30 and imc<40:
	print "Obesidad"

else: 
	imc>=40
	print "Obesidad morbida"
