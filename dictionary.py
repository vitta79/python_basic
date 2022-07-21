from itertools import product

monthdictionary={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}
print(monthdictionary)
print(monthdictionary["Dec"])
print(monthdictionary.get("Jan"))
print(monthdictionary.pop("Jan"))
print(monthdictionary.get("Mon","The default value"))

i=9
while i>0:
    print(i)
    i-=2
