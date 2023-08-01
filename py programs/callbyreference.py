List1 = [2, 4, 6]
List2 = List1
List1.append(8) #Both List1 and List2 are changed
print (List1)
print (List2)

List1= List1 + [10]
print (List1) #List 1 is changed
print (List2) #List 2 remains same, since copy of List 1 is only made
