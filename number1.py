x = []
a = []
z = int(input())
for i in range(z):
	x.append(i+1)
n = 0
for i in x:
	if x[n] % 2 == 0:
		x.remove(x[n])
	n += 1
g = 0
i = 0		
for i in range(len(x)):
	if i %500 == 0:
		print(i*2)
	n = 1
	y = 0
	while n <= x[g]:
		#print(i,x[g],n,x)
		if x[g] % n == 0:
			y += 1
		n += 1
	if y > 2:
		x.remove(x[g])
		g-=1
	g += 1	
n = 0
for i in x:
	if n + 1 < len(x):
		if x[n+1] - x[n] == 2:
			a.append(x[n])
			a.append(x[n+1])
	n += 1
print("Number of prime numbers - ",len(x),"The ratio of all numbers to primes -",z/len(x))
print(len(x),len(a)," - ",str(int((len(a)/len(x))*100))+"%", len(a)/z)

