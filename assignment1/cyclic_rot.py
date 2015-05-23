def is_cyclic_rotation(a,b):
	print  "Yes they are cyclic rotation of one another " if(len(a)==len(b) and (a+a).find(b)!=-1) else "No they are not cyclic rotation of one another"
is_cyclic_rotation(raw_input("Enter first string  :  "),raw_input("Enter second string  :  "))