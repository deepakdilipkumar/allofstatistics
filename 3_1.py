import random

ss = [-1,1]
runlength=100
reward=1
trials=10000
avgreward=0.0

for i in range(trials):
	reward=1
	for j in range(runlength):
		reward*=pow(2,random.choice(ss))
	avgreward+=reward

print(avgreward/trials)
print(pow(1.25,runlength))