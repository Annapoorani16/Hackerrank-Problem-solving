#Write a program to give the following output for the given input
#The number varies from 1 to 99.
#Eg 1: Input: a1b10
      # Output: abbbbbbbbbb 
a=input()
i=0
try:
 while(i<(len(a)-1)):
    if(a[i+2]>="0" and a[i+2]<="9"): #checking whether double dig exit
        print(a[i]*int(a[i+1]+a[i+2]),end="")
        i+=3
    else:                             #else print the alpha with adjacent dig
        print(a[i]* int(a[i+1]),end="")
        i+=2
except IndexError:                    #if indexerror occurs
    print(a[i]* int(a[i+1]),end="")
    
