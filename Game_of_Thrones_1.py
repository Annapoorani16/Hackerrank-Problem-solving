s="aaabbbb" #if palindrome exist
d1=0;b=0
for ele in s:
     if(s.count(ele)%2!=0 and (b!=ele)): #checking odd char count is more than 1
         d1+=1
         b=ele
if(d1>1):
     print("NO")
else:
     print("YES")
