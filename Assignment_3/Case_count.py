string=input('enter the string to be reversed: ')

def case_count(str):
    
    upper_count=0
    lower_count=0
    for i in str:
        if(i.isupper()):
            upper_count=upper_count + 1
        elif(i.islower()):
            lower_count=lower_count + 1
      
    print("No of Uppercase characters: ",upper_count,
    "\nNo of Lowercase characters: ",lower_count)    
        
    
case_count(string)