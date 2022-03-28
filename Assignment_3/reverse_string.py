string=input('enter the string to be reversed: ')

def reverse_string(str):
    rev=''
    i=len(str)-1
    while(i>=0):
        rev= rev + str[i]
        i-=1
    print(rev)    
        
    
reverse_string(string)  