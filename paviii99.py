d1=int(input())
for i in range(0,d1):
	if 2**i==d1 or d1==1:
		print("yes")
		break
else:
	print("no")
