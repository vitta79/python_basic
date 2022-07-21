# a=b*c+d
# d=a-b*c
def gcd(a, b):
    if a == 0:
        return b
    diziA.append(b)
    diziB.append(int(b / a))
    diziC.append(a)
    diziD.append(int(b % a))
    return gcd(b % a, a)


diziA = [0]
diziB = [0]
diziC = [0]
diziD = [0]

a=24
b=138
gcds = gcd(a, b)

for i in len(diziD):
    print(str(diziD[i]))


print(diziA)
print(diziB)
print(diziC)
print(diziD)
print(str(len(diziD))+str(diziD[3]))

