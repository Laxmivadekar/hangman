l1 = [2,4,3]
l2 = [5,6,4]
i=1
a=''
b=''
while i<=3:
    a+=str(l1[-i])
    b+=str(l2[-i])
    i=i+1
print(a)
print(b)
c=int(a)+int(b)
d=str(c)
i=1
l=[]
while i<=3:
    a=d[-i]
    b=int(a)
    l.append(b)
    i=i+1
print(l)





# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
