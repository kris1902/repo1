class input_tekstu():
	"""Klasa do pracy na tekscie"""
	def __init__(self):
		self.lista=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	def liczenie(self, nazwa):
		"""Funkcja do zliaczania slow o danej dlugosci"""
		dane=open(nazwa+".txt").read()
		dane=dane.replace(",","")
		dane=dane.replace(".","")
		dane=dane.replace(";","")
		dane=dane.replace(":","")
		dane=dane.replace("\n"," ")
		dane=dane.replace("!", "")
		podziel=dane.split(" ")
		print podziel
		for i in podziel:
			if len(i)-1==(-1):
				pass
			else:
				self.lista[len(i)-1]+=1
		print self.lista
		return self.lista

if __name__=="__main__":
	it=input_tekstu()
	it.liczenie("plik")
