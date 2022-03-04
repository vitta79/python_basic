def sayhi():
    print("Hello User")
def sayhiwith(name):
    print("Hello "+name)
def sayhi_with(name,age):
    print("Hello "+name+" you are "+str(age))
def cube(num):
    return pow(num,3)

sayhi()
sayhiwith("Mike")
sayhi_with("John",45)
print(str(cube(3)))

def fact(num):
    if num<1:
        return 1
    return num*fact(num-1)
val=int(input("Factorial: "))
print(str(val)+" factorial is: "+str(fact(val)))

# if else state
is_male=True
is_tall=True
if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You are neither male nor tall")
if is_male:
    print("You are male")
elif is_tall:
    print("You are tall")
else:
    print("You are not male or tall")