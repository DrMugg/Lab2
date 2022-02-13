import numpy as matrix
import sys
import matplotlib.pyplot as plt

def makelist(x1,y1,z1,z2):
	x=[x1]
	y=[y1]
	while z1<z2:
		x.append(x1+y1*z1)
		z1+=1
	return x

def temperature(b, m, temp):
	return b + m * temp

def powers(lin,a,b):
	lout=[]

	for i in lin:
		i=float(i)
		templist=[]
		aa=a
		while aa<=b:
			templist.append(i**aa)
			aa+=1
		lout.append(templist)
	return matrix.array(lout)

def main():
	inputtxt="chirps.txt"
	if len(sys.argv)>1:
		inputtxt=sys.argv[1]
		if len(sys.argv)>2:
			n=sys.argv[2]
	xy=matrix.transpose(matrix.loadtxt(inputtxt))
	X=xy[0]
	Y=xy[1]
	Xp  = powers(X,0,n)
	Yp  = powers(Y,1,1)
	Xpt = matrix.transpose(Xp)
	a= matrix.matmul(matrix.linalg.inv(matrix.matmul(Xpt,Xp)),matrix.matmul(Xpt,Yp))
	a=a[:,0]

	#implementera poly enligt uppgift och ändra x-värden
	mt=makelist(b,m,1,len(X))
	x = [min(X), max(X)]
	y = [temperature(b, m, temp) for temp in x]
	plt.plot(X,Y,'ro')
	plt.plot(x,y)
	plt.show()
main()