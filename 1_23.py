import random

trials=10000
samplespace=[1,2,3,4,5,6]
A=0.0
B=0.0
AB=0.0

for i in range(trials):
	outcome=random.choice(samplespace)
	if outcome==2 or outcome==4 or outcome==6:
		A+=1

	if outcome==1 or outcome==2 or outcome==3 or outcome==4:
		B+=1
	
	if outcome==2 or outcome==4:
		AB+=1


A/=trials
B/=trials
AB/=trials

print "P(A) = ", A, "\n", "P(B) = ", B, "\n", "P(AB) = ", AB, "\n", "P(A)*P(B) = ", A*B