import szablon_programu

def histogram(nazwa):
                """Funkcja tworzaca histogram."""
                it = szablon_programu.input_tekstu()
		lista = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                histogram = []
                lista = it.liczenie(nazwa)
		for i in lista:
                        histogram.append(i*"=")
                return histogram

print histogram("plik")
