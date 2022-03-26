l1=input("enter the characters")
le=len(l1)
l2=''
for i in l1:
    l2+=l1[le-1]
    le=le-1
print(l2)  