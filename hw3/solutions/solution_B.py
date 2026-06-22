n = int(input())
def phib(num):
	if num == 1 or num == 2:
		return 1
	else:
		return(phib(num - 1) + phib(num - 2))
print(phib(n))
	
