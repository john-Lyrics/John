def is_even(x): return x %2==0
numbers=[1,56,234,87,4,76,24,69,90,135]
print(list(map(is_even, numbers)))
print(list(map(is_even, numbers)))
print(list(filter(is_even, numbers)))

 