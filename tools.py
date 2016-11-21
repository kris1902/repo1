def sprawdz(lista):
	"""sprawdzenie czy podana zostala lista z wlasciwymi parametrami"""
	if type(lista)==list or type(lista)==tuple:
		for i in lista:
			if type(i)!=float and type(i)!=int:
				return False
		return True
	return False

if __name__=="__main__":
	lista1=[1,2,3]
	lista2=(1,2,3)
	lista3=["a",1,2]
	print sprawdz(lista1)
	print sprawdz(lista2)
	print sprawdz(lista3)
