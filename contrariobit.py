def ultimo(x):
	return x[len(x)-1] #Restituisco l'ultimo elemento della lista

def contrario(x):
	return [x[0],] if len(x)==1 else[ultimo(x),]+contrario(x[0:len(x)-1]) 
