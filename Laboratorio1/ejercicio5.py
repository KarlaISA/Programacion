#Karla Ivonne Serrano Arevalo
#Ejerercicio 1
#22 noviembre 2016

segundos=input("Total de segundos: ")

dias=segundos/86400
horas=segundos/3600-24*dias
minutos=segundos/60-1440*dias-60*horas
segundos=segundos-86400*dias-3600*horas-60*minutos

print "Tiempo total viejando en segundos es: ",dias,"dias",horas,"horas",minutos,"minutos",segundos,"segundos"


