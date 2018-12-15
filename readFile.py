file = open('readMe.txt', 'r+')
#for each in file:
 #   print(each)


#print(file.read())

print(file.read())
list = file.read()
print("List: ", list)
file.write("Add another thing.")
file.close()
file = open('readMe.txt', 'r')
print(file.read())
file.close()
