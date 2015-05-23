sieve=[]
def get_prime(n):
	for i in range(2,n+1):
		sieve.append(i)

	p=2
	while(p!=sieve[-1]):
		i=2
		while (i*p<=sieve[-1]):
			if(i*p in sieve):
				sieve.remove(i*p)
			i+=1
		p=sieve[sieve.index(p)+1]

	print sieve

n=input("Enter an integer  :  ")
get_prime(n)