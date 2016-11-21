#
from math import sqrt
from IBeBack import *
from tools import *

def srednia(lista):
	"""isrednia"""
	sprawdzenie=sprawdz(lista)
	if sprawdzenie==True:
		if type(lista) != list:
			raise IBeBack
		suma=0.0
		for i in lista:
			suma+=i**2
		return sqrt((suma/len(lista)))
	return "Podano zly typ danych wejsciowych"

def srednia_ar(lista):
	"srednia arytmetyczna"
	i=0
	sum=0
	for i in range(lista):
		sum+=i
		i+=1
	return sum/i


print("proba 1")
print srednia([1,2,3,4])
print("proba 2")
print srednia("ala") 
