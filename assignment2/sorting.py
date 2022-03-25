[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
length=len(a)
for i in range(length):           
    for j in range(length-i-1):
        if(a[j][-1] > a[j+1][-1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)  