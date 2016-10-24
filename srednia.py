from math import sqrt
from IBeBack import *

def srednia(lista):
	"""isrednia"""
	if type(lista) != list:
		raise IBeBack
	suma=0.0
	for i in lista:
		suma+=i**2
	return sqrt((suma/len(lista)))
print("proba 1")
print srednia([1,2,3,4])
print("proba 2")
print srednia("ala") 
