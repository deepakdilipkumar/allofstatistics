import numpy.random as rnd
import numpy as np

B=100000
N1=50
N2=50

p1mle=0.3	
p2mle=0.4
taumle=p2mle-p1mle

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

t=-10

estimate=np.array(estimate)

allt=[0.01*t for t in xrange(-5000,5000)]

target=0.95
tol=0.01

for t in allt:
	cur=np.mean(np.sqrt(N1+N2)*(estimate-taumle)<t)
	if(np.abs(target-cur)<tol):
		print(t)
		print(cur)
		break