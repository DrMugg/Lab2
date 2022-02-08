def powers(lin,a,b):
	lout=[]
	
	for i in lin:
		templist=[]
		aa=a
		while aa<=b:
			templist.append(i**aa)
			aa+=1
		lout.append(templist)
	return lout

def transpose(matrisin):
	matrisut=[]
	m=len(matrisin)
	n=len(matrisin[m-1])
	for i in range(n):
		matrisut.append([])
		for k in range(m):
			matrisut[i].append(matrisin[k][i])
	return matrisut

def matmul(s1,s2):
	i=len(s1)
	k=len(s1[0])
	j=len(s2[0])
	c=[]
	for ii in range(i):
		c.append([])
		for jj in range(j):
			temp=0
			for kk in range(k):
				temp+=s1[ii][kk]*s2[kk][jj]
			c[ii].append(temp)
	return c

def printmatrix(matris):
	for m in matris:
		print(m)

def invert(A):
	det=A[0][0]*A[1][1]-A[1][0]*A[0][1]
	print(A)
	print(det)
	return [[A[1][1]/det,-A[0][1]/det],[-A[1][0]/det,A[0][0]/det]]

def loadtxt(open_file): 
	f=open(open_file)
	lista=list(f)
	f.close()
	listaut=[]
	for i in lista:
		listaut.append(str(i).split())
	return listaut

def makenumber(strang):
	token=[]
	
	for i in strang:
		start=0
		end=0
		chars=list(i)
		while end<len(chars):
			if chars[end].isdigit():
				while end<len(chars) and (chars[end].isdigit() or chars[end]=="."):
					end=end+1
				token.append("".join(chars[start:end]))
				start=end
				continue
			else:
				token.append(chars[end])
				end=end+1
				start=end
	i=0
	while i<len(token):
		if i=="\t" or i=="\n":
			token[i].pop()
		i+=1
	return token


# s1=[[0,1],[1,0]]
# s3 = [[1, 0],[0,-1]]
#I = [[1,0,0],[0,1,0],[0,0,1]]

#printmatrix(matmul([[1, 2, 3], [4, 5, 6],[7, 8, 9]],I))
#printmatrix(matmul(s1,s3))
#printmatrix(matmul([[1,2],[3,4]],invert([[1,2],[3,4]])))

#print(loadtxt("chirps.txt"))


#print(transpose([[1,2],[3,4],[5,6]]))
#print(powers([2,3,4],0,2))