import matrix
import sys
import matplotlib.pyplot as plt
def makelist(x,y,z1,z2):
	x=list(x)
	y=list(y)
	while z1<z2:
		x=x+y*z1
		z1+=1
	return x
def main():
	inputtxt="dataset1.txt"
	if len(sys.argv)>1:
		inputtxt=sys.argv[1]
	xy=matrix.transpose(matrix.loadtxt(inputtxt))
	X=xy[0]
	Y=xy[1]
	Xp  = matrix.powers(X,0,1)
	Yp  = matrix.powers(Y,1,1)
	Xpt = matrix.transpose(Xp)

	[[b],[m]] = matrix.matmul(matrix.invert(matrix.matmul(Xpt,Xp)),matrix.matmul(Xpt,Yp))
	print([[b],[m]])
	mt=makelist(b,m,0,100)
	plt.plot(b,mt)
	plt.show()
main()

def makelist(x,y,z1,z2):
	x=list(x)
	y=list(y)
	while z1<z2:
		x.append(x+y*z1)
		z1+=1
	return x