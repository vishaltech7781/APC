a = frozenset([1,2,3,4,5,6])
b = frozenset([5,6,7,8,9])

print("Union:",a.union(b))
print("Intersection:",b.intersection(a))
print("Difference:",a.difference(b))
print("Symmetric Difference:",a.symmetric_difference(b))
print("Is Subset:",a.issubset(b))
print("Is Superset:",b.issuperset(a))
print("Is Disjoint:",a.isdisjoint(b))

#iteration
for i in a:
    print(i)

for i in b:
    print(i)