import os

def makeFile(fileName, message, mode):
    a = open(fileName, mode)
    a.write(message)
    a.close()

def openFile(fileName):
    b = open(fileName, "r")
    lines = b.readlines()
    for line in lines:
        print(line)
    b.close()

makeFile("fileFirst.txt", "This is my first file1\n", "w")
makeFile("fileFirst.txt", "This is my first file2\n", "w")
makeFile("fileFirst.txt", "This is my first file3\n", "w")
makeFile("fileSecond.txt", "This is my Second file1\n", "a")
makeFile("fileSecond.txt", "This is my Second file2\n", "a")
makeFile("fileSecond.txt", "This is my Second file3\n", "a")

print("write fileFirst.txt")
print("-------------------------------------")
openFile("fileFirst.txt")
print("-------------------------------------")

print("\n")

print("write secondFirst.txt")
print("-------------------------------------")
openFile("fileSecond.txt")
print("-------------------------------------")



