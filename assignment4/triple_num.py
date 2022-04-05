

num=input('enter the values with spaces: ')
a=num.split()
for i in range(len(a)):
    a[i]=float(a[i])

def triple_number(list):
    return(list * 3)

map_triple=map(triple_number,a)   
print(list(map_triple))
   