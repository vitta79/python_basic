def primeNumbers(num):
    prime=2
    arr=[2]
    while prime<num:
        i=2
        isit=True
        while i<prime:
            if prime%i==0:
                isit=False
                break
            i+=1
        if isit==True:
            arr.append(prime)
        prime+=1
    return arr

def isPrime(num):
    arr=primeNumbers(num-1)
    isit=True
    for n in arr:
        if num%n==0:
            isit=False
            break
    if isit==True:
        return 1
    else:
        return 0
def fileIn():
    try:
        file1 = open("primeOrNot.txt", "w")
        i = 0
        print("To finish adding number push -1")
        i = int(input("Number: "))
        while i > -1:
            file1.write(str(i) + "\n")
            i = int(input("Number: "))
    except:
        print("Invalid Value")
    file1.close()

fileIn()
file1=open("primeOrNot.txt","r+")
arr=file1.read().split("\n")
i=0
while i<len(arr):
    arr[i]=arr[i]+"-/-"+str(isPrime(int(arr[i])))
    i+=1

file1.writelines(arr)
print(file1.read())
file1.close()


