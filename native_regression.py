import matrix
import sys
def main():
	inputtxt="dataset1.txt"
	if len(sys.argv)>1:
		inputtxt=sys.argv[1]
	xy=matrix.transpose(matrix.loadtxt(inputtxt))
	print(inputtxt)
	X=[0]
	Y=[1]
	Xp  = matrix.powers(X,0,1)
	Yp  = matrix.powers(Y,1,1)
	Xpt = matrix.transpose(Xp)

	[[b],[m]] = matrix.matmul(matrix.invert(matrix.matmul(Xpt,Xp)),matrix.matmul(Xpt,Yp))
main()