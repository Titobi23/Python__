# Writing a file
# r is for read
# r+ is for reading and writing
# w is for writing
# wb is for writing in binary
with open("family.txt", "wb") as myFile:
    myFile.write(b"Tolu\n")
    myFile.write(b"Feranmi\n")
    myFile.write(b"Mommy\n")
    myFile.write(b"Dad\n")
    myFile.write(b"Leticia\n")
    myFile.write(b"Goldfield\n")
print("Just wrote the file:", myFile.name)
print("Opened file in mode:", myFile.mode)
myFile.close()