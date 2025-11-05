s = {1, 2}
s1 = {11,22,33,4,3}

s.add(3)
s.add(4)
s.add(5)
s.add(7)
print(s)  

s.remove(3)
print(s)

s.discard(6)  # No error even though 5 is not in set
print(s)      

s.pop()
print(s)

print(s.union(s1))

print(s.intersection(s1))  

print(s.difference(s1))  

s2 = s1.copy()
print(s2)
