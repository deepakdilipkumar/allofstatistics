import numpy.random as rnd 
import numpy as np

B=100000
X=30
Y=40
n=50

estimate=[]
for i in range(B):
	p1=rnd.beta(X+1,n-X+1)
	p2=rnd.beta(Y+1,n-Y+1)

	estimate.append(p2-p1)

print(np.mean(estimate))
print(np.std(estimate))