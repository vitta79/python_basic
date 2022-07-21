from typing import List

tuparr=(44,85,96,57)
intarr=[12,5,9]
strarr=["Winter","Spring","Summer","Autumn"]
intarr
print(intarr)
print(strarr)
print(str(intarr[2])+" "+strarr[3])
intarr[1]=45
#tuparr[1]=45  we can't change the value of tuples so we will get an error
print(str(intarr[1])+" "+str(tuparr[1]))