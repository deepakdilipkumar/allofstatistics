import random
import matplotlib.pyplot as plt

p=0.3
headsfreq=[]
maxtrials=10000

for n in range(maxtrials):
	heads=0.0
	for i in range(n+1):
		if(random.random()<=p):
			heads+=1

	headsfreq.append(heads/(n+1))

#print(headsfreq)
plt.plot(range(maxtrials),headsfreq)
plt.xlabel("Number of trials averaged over")
plt.ylabel("Frequency of heads")
plt.show()
