import numpy as np
f = open("ReceivedMessages.txt","r")
#print(f.read())
text = f.read()
#print(text[1])
#num=""
d={0:" "}
lkey=[]
lvalue=[]
count=0
flag = 0
str1 = ""
str2=""
str3=""
with open("ReceivedMessages.txt") as f:
    for line in f:
        if count%7==0:
            flag = 1
            x = line[:10]
        else:
            if flag == 1:
                lkey.append(x+" "+line[:3])
                flag = 0
            else :
                 lvalue.append(line[2:3]+" ")

        count = count+1
i=1
for l in lvalue:
        #print(l)
        if i<=5:
            str1 = str1+l
        elif i<=10:
            str2 = str2+l
        else:
            str3 = str3+l
        i = i + 1

dict ={lkey[0]:str1,lkey[1]:str2,lkey[2]:str3}

print(dict)

