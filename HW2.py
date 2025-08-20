# Simple Student Grade Management

students = []
grades = []

# Add students
students.append("Alice")
grades.append(85)

students.append("Bob")
grades.append(90)

students.append("Charlie")
grades.append(78)

# Update grade
students[0] = "Alice"   # same student
grades[0] = 88

# Remove a student (Charlie)
index = students.index("Charlie")
students.pop(index)
grades.pop(index)

# Average grade
avg = sum(grades) / len(grades)

# Highest and lowest
highest = max(grades)
lowest = min(grades)

# Results
print("Students:", students)
print("Grades:", grades)
print("Average grade:", avg)
print("Highest grade:", highest)
print("Lowest grade:", lowest)
