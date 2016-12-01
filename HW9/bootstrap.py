import numpy.random as rnd
import numpy as np

B=100000
N1=50
N2=50

p1mle=0.6	
p2mle=0.8

estimate=[]

for i in range(B):

	p1=0.0
	for j in range(N1):
		if(rnd.uniform(0,1)<p1mle):
			p1+=1

	p1/=N1

	p2=0.0
	for j in range(N2):
		if(rnd.uniform(0,1)<p2mle):
			p2+=1

	p2/=N2

	estimate.append(p2-p1)

print(np.std(estimate))
print(np.mean(estimate))