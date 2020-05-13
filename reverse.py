#A program to reverse every word of a string and display the reversed string as an output. 
#For example, if we input a string as “Reverse the word of this string” then the output of the
 #program would be: “esrever eht drow fo siht gnirts”.

n=input()
words=n.split() #splitting the sentence & store as single word
for ele in words:
    print(ele[::-1],end=" ") #reversing each word using slicing
