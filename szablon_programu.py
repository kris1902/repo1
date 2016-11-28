class input_tekstu():
	def __init__(self):
		self.lista=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	def liczenie(self, nazwa):
		dane=open(nazwa+".txt").read()
		podziel=dane.split(" ")
		for i in podziel:
			self.lista[len(i)-1]+=1
		return self.lista

if __name__=="__main__":
	it=input_tekstu()
	it.liczenie(plik.txt)
