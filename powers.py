def powers(lin,a,b):
	lout=[]
	for i in lin:
		while a<b:
			lout.append(lin[i]**a)
			a+=1
	return lout