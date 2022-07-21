num=int(input("the number: "))
pow=int(input("the power: "))

# basic power
result=num**pow
print("Result: " +str(result))

# with for loop
result=1
for n in range(pow):
    result=result*num
print("Loop Result: " +str(result))