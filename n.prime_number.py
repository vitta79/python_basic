
num=int(input("How many Prime number: "))
prime=1
arr=""
while num>0:
   i=2
   isit=True
   while i<prime:
       if prime%i==0:
           isit=False
           break
       i+=1
   if isit==True:
       arr = arr + " " + str(prime)
       num-=1
   prime+=1
print(arr)