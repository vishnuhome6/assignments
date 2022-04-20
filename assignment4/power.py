num=float(input("enter the number :"))
n=int(input("enter the power :"))

class Power_number:
  
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def power(self):
        result=self.b ** self.a
        print(result)

obj=Power_number(n,num)
obj.power()