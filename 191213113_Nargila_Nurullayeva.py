def gcdOklid(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdOklid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

a=int(input("a:"))
b=int(input("b:"))
g, x, y = gcdOklid(a, b)
print("gcd(",a,",",b,") =",g,"\n",g,"=",x,"*",a,"+(",y,")*",b,". Buradan x=",x," ve y=",y," bulunur")
