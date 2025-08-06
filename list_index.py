list= []

n = int(input("how many elements u want to append?"))

for i in range(0,n):
    items = input(f"enter the elements no.{i}:")
    list.append(items)

print(list)

print(list[0])
print(list[2])
print(list[:2])
print(list[::])
print(list[1:])
print(list[-1])
print(list[-3])
print(list[0:3])
print(list[-4:-1])