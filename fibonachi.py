def fib_rec(n):
    if n<= 1 :
        return n
        
    else :
        return fib_rec(n-1) + fib_rec(n-2)
        
    

print(fib_rec(10))
print(list(map(fib_rec, range(1,11))))