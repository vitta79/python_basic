
num1=input("First number: ")
num2=input("Second number: ")
opt=input("Operator: ")

while opt!='e':
    if(opt=='+'):
       result=float(num1)+float(num2)
    elif(opt=='-'):
     result=float(num1)-float(num2)
    elif(opt=='*'):
        result=float(num1)*float(num2)
    elif(opt=='/'):
        result=float(num1)/float(num2)
    print(num1+opt+num2+"="+str(result))
    num1 = input("First number: ")
    num2 = input("Second number: ")
    opt = input("Operator: ")