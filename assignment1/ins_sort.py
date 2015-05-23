array=[]
print "Enter no of elements in the array"
n=input()
print "Enter %d numbers " %n
for i in range(n):
	array.append(input())
## Insertion sort
for i in range(1,n):
	temp=array[i]
	j=i-1
	while temp<array[j] and j>=0:
		array[j+1]=array[j]
		j-=1
	array[j+1]=temp
print "Sorted array :"
print array