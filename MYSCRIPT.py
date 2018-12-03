f = open("test2.txt", "w+")
f.write("This is my text file")
f.close()
 
f = open("test2.txt", "r")
s = f.read()
print s
