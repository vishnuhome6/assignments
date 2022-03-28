n=int(input("enter the no. of elements present in the list: "))
list=[]

for i in range(n):
    t=float(input('enter the numbers in the list' ))
    list.append(t)

def sum_list(num):
    sum=0
    for i in num:
        sum=sum+i
    print(sum)


sum_list(list)