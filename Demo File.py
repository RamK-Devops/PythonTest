file1 = open('test.txt')

#print(file1.read()) #read all records

#print(file1.read())  read only 3 chars

#print(file1.readline())  #read one single line
#print(file1.readline())

record = file1.readline()
while record != "":
    print (record)
    record = file1.readline()

file1.close()

