
def even_fibo():
	print "Enter an integer n"
	n=input()
	term1=0
	term2=1
	term3=term1+term2
	print "Even fibonacci numbers less than or equal to %d" %n
	while term3<=n:
		if(term3%2==0):
			print term3
		term1=term2
		term2=term3
		term3=term1+term2

even_fibo()