import numpy as matrix
import sys
import matplotlib.pyplot as plt

def makelist(x1,y1,z1,z2): #skapar en lista från z1 till z2 enligt linjärekvation x1=m y1=k z1=x
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

def poly(a, x, n):
	out=[]
	if len(a)<n:
		n=len(a)
	for i in range(0,len(x)):
		temp=0
		for exponent in range(0,n+1):
			temp+=a[exponent]*x[i]**exponent
		out.append(temp)
	return out

def main():
	inputtxt="chirps.txt"
	n=3
	if len(sys.argv)>1:
		n=sys.argv[len(sys.argv)-1]
		inputtxt=sys.argv[1]
		if len(sys.argv)>2:
			n=int(sys.argv[2])
	xy=matrix.transpose(matrix.loadtxt(inputtxt))
	X=xy[0]
	Y=xy[1]
	Xp  = powers(X,0,n)
	Yp  = powers(Y,1,1)
	Xpt = matrix.transpose(Xp)
	a= matrix.matmul(matrix.linalg.inv(matrix.matmul(Xpt,Xp)),matrix.matmul(Xpt,Yp))
	a=a[:,0]
	#implementera poly enligt uppgift och ändra x-värden
	Xvarden=matrix.linspace(min(X),max(X),40).tolist()
	Yvarden=poly(a,Xvarden,n)
	x = [min(X), max(Xvarden)]
	print(len(Yvarden),len(X))
	plt.plot(X,Y,'ro')
	plt.plot(Xvarden,Yvarden)
	plt.show()
main()