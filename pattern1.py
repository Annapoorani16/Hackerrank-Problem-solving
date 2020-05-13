#printing pattern
#Eg:I/P=2987
#O/P: 22998877
    # 22998877
n=int(input())
l=str(n) #converting to string
for _ in range(int(l[:1])): #setting range upto 1st element in n
    for ele in l:
        print(ele*(int(l[:1])),end="") #print every element(upto 1st ele in n times)
    print()                         
