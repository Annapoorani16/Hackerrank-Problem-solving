#single integer must denote the minimum number of characters which must be deleted to make the two strings anagrams of each other.
s1="cde"
s2="abc"
c=(set(s1).intersection(set(s2))) #Finding com char
com_char=0
for ele in c:
    if((s1.count(ele))<=(s2.count(ele))): #Finding the com char count &
        com_char+=(s1.count(ele))           # comparing the count
    elif((s1.count(ele))>(s2.count(ele))):
        com_char+=(s2.count(ele))
print((len(s1)-com_char)+(len(s2)-com_char)) #subracting the com_char frm s1 &s2
                                               #&finding the deletions



        

