import matrix
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

def main():
	inputtxt="chirps.txt"
	if len(sys.argv)>1:
		inputtxt=sys.argv[1]
	xy=matrix.transpose(matrix.loadtxt(inputtxt))
	X=xy[0]
	Y=xy[1]
	Xp  = matrix.powers(X,0,1)
	Yp  = matrix.powers(Y,1,1)
	Xpt = matrix.transpose(Xp)
	[[b],[m]] = matrix.matmul(matrix.invert(matrix.matmul(Xpt,Xp)),matrix.matmul(Xpt,Yp))
	mt=makelist(b,m,1,len(X))
	x = [min(X), max(X)]
	y = [temperature(b, m, temp) for temp in x]
	plt.plot(X,Y,'ro')
	plt.plot(x,y)
	plt.show()
main()

