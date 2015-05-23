from heapq import merge

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) / 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))
arr=[]
size=input("Enter size of array  :  ")
print "Enter %d numbers seperated by enters" %size
for i in range(size):
	x=input()
	arr.append(x)
print "Sorted array is : "
print merge_sort(arr)
