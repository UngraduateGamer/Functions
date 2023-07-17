def calculate_Geometric_mean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isGreater(a,b):
    if(a>b):
        print(a,"is Greater")
    elif(a==b):
        print("Both are Equals")
    else:
        print(b,"is Greater")
        
num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))
calculate_Geometric_mean(num1,num2)
isGreater(num1,num2)
