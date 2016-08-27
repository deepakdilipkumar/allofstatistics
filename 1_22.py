import random

p=0.3
n=100
trials=1000 	

avgX=0.0
	
for i in range(trials):
	X=0
	for j in range(n):
		if(random.random()<p):
			X+=1

	avgX+=X

avgX/=trials
print avgX, "\t", n*p