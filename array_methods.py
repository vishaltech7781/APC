import array #type: ignore

a1 = array.array("i", [1,1, 2,2, 3, 4, 5])
a2 = array.array("i", [33])

# append a new element
a1.append(7)
a1.pop(4)
a1.remove(2)
print(a1.index(5))
print(a1.count(1))
print(a1.reverse())

a1.extend(a2)
a1.insert(3,22)

for j in a1:
    print(j,end=" ")


