 for a in range(5,0,-1):
	for m in range(a):
		print(" ",end="")
	print("*",end="")
	for n in range((5-a)*2):
		print(" ",end="")
	print("*")
for a in range(6):
	for m in range(a):
		print(" ",end="")
	print("*",end="")
	for n in range((5-a)*2,0,-1):
		print(" ",end="")
	print("*")

