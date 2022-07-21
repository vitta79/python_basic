file1=open("file1.txt","r")
# is file readable or not. it returns bool type true or false
print(file1.readable())
# reads next line of txt
print(file1.readline())
# it prints file like array
print(file1.readlines())
# with seek(0) file starts to read at beginnig
file1.seek(0)
print("\nwrite full txt")
print(file1.read())
file1.seek(0)
print("\nwrite using for loop")
for line in file1.readlines():
    print(line)
file1.close()

# Writing to files
file2=open("file2.txt","w")
file2.write("file2 is  new file. When we open a file with 'w' we overwrite in existing file")
file1=open("file1.txt","a")
file1.write("file1 is existing file and we can add some phrases to it with 'a' it means append")
