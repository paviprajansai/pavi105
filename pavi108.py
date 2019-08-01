n11,k11=map(int,input().split())
l=list(map(int,input().split()))
s11=sorted(l)
c11=0
for i in range(0,len(s11)):
	c11=c11+1
	if c11==k11:
		print(s11[i])
