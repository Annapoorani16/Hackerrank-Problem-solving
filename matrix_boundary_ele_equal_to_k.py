#accept a matrix of size n*m & integer k
#check all boundary elements are equal to k
#if yes print "yes" else "no"
import numpy
n,m,k = map(int,input().split()) # getting inputs
a=numpy.array([[int(j) for j in input().split()[:m]]for  _  in range(n)]) #getting array inputs
if((list(a[0,:]).count(k)==m)and (list(a[n-1,:]).count(k)==m)and(list(a[:,0]).count(k)==n) and (list(a[:,m-1]).count(k)==n)): #slicing all boundary elements & checking all elements are equal to k
    print("Yes")
else:
    print("No")
