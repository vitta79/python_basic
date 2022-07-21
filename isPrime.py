def isPrime(prime):
    i=1
    while i<prime:
        if i>1:
            if prime%i==0:
                return False
        i+=1
    return True

print("Is number prime: " + str(isPrime(int(input("the number: ")))))
