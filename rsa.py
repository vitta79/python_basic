import random


#   Asal olup olmadigi kontrolu
def isPrime(prime):
    i = 1
    while i < prime:
        if i > 1:
            if prime % i == 0:
                return False
        i += 1
    return True


#   Asal sayi olusturma
def asalCreate(k, b):
    a = random.randint(k, b)
    while (isPrime(a) != True):
        a = random.randint(3, 100)
    return a


#   Formuldeki d degerini bulmak icin Oklid algoritmasi
def gcdOklid(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdOklid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


#   Encryption Sifreleme algoritmasi
#   c=m^e mod n
def encMesaj(metin):
    i = 0
    ch = 0
    donen = ""
    while (i < len(metin)):
        if (metin[i] != " "):
            ch = ord(metin[i])
            ch = pow(ch, e) % n
            donen += chr(ch)
        else:
            donen += metin[i]
        i += 1
    return donen


#   Deccryption Sifre Cozme algoritmasi
#   m=c^d mod n
def decMesaj(metin):
    i = 0
    ch = 0
    donen = ""
    while (i < len(metin)):
        if (metin[i] != " "):
            ch = ord(metin[i])
            ch = pow(ch, d) % n
            donen += chr(ch)
        else:
            donen += metin[i]
        i += 1
    return donen


p = asalCreate(3, 100)
q = asalCreate(3, 100)

n = p * q
tot = (p - 1) * (q - 1)
e = asalCreate(3, tot)

#   x degeri e`nin tersidir ve sonuc olarak x, d`ye esittir
#   e*d=1 mod(tot)<=>e*e^-1=1 mod(tot)
gcdEvT, x, y = gcdOklid(e, tot)
d = x

#   Eger x degerimiz negatif bir deger ise, pozitif d degeri elde etme
while (d < 0):
    d += tot

print("p: ", p, " q: ", q, " n: ", n, " tot: ", tot, " e: ", e, " d: ", d)

mesaj = input("Mesajı giriniz: ")
enc=encMesaj(mesaj)
dec=decMesaj(enc)
print("Mesaj: ", mesaj, " \nŞifrelenmiş: ",enc," \nŞifre Çözülmüş: ",dec)
