
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    try:
        return x/y
    except:
        print("Your dividing number by zero")
while True:
    print("Select operation\n","1.Add\n","2.Subtract\n","3.Multiply\n","4.Divide\n")
    choice=int(input("Enter your choice\n"))
    num1=int(input("Enter the first number\n"))
    num2=int(input("Enter the second number\n"))
    if choice in (1,2,3,4):
        if choice ==1:
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice==2:
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice==3:
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice==4:
            print(num1,"/",num2,"=",divide(num1,num2))
        else:
            print("Invalid operation")
    if "no"==input("Lets do next calculation(yes/no)\n"):
        break
        
    