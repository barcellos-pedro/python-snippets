# List Comprehension Structure
# (values) = [ (expression) for (value) in (collection) ]

# Example 1
numbers = [*range(10)]
squares = [x * x for x in numbers]
print(squares)

# Common for loop
squares2 = []
for x in numbers:
    squares2.append(x * x)
print(squares2)

# Example 2
people = ["Ana", "Pedro", "Lele", "Giggio"]

hello_names = [f'Hello {name.lower()}' for name in people]
lower_names = [name.lower() for name in people]

print(hello_names)
print(lower_names)

# Filter
filtered_names = [name for name in people if name.endswith('o')]
filtered_numbers = []
print(filtered_names)
