numbers=[12, 54, 33, 67, 24, 89, 11, 24, 47]
print(list(filter(lambda even: even%2==0  ,numbers)))

[n for n in numbers if n%2==0]
