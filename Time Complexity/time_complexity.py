import time
def num(m):
	t1 = time.time()
	for i in range(0,m):
		print(i)
	t2 = time.time()
	print(str(t2-t1))
num(3)
