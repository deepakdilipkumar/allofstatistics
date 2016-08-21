import random

p=0.3
headsfreq=[]

for n in range(10000):
	heads=0.0
	for i in range(n+1):
		if(random.random()<=p):
			heads+=1

	headsfreq.append(heads/(n+1))

print(headsfreq)