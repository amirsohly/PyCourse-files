#CREATE
'''f = open("test.txt","x")'''

#DELETE
'''import os
os.remove("test.txt")'''

'''import os
if os.path.exists("test1.txt"):
    os.remove("test1.txt")
    print("DELETED")
else:
    print("Error")'''

#WRITE
'''f = open("test.txt","a")
f.write("Salam. Man Amirreza Hastam.")'''

'''f = open("test.txt","w")
f.write("Hello")'''
#f.close()

#READ
f = open("test.txt", "r")
print(f.read())
#print(f.read(3))
'''print(f.readline())
print(f.readline())'''

'''for x in f:
    #print(x)
#f.close()'''