#Recursive function
def fib(n):
    if n == 1:
        return 1
    elif n ==2:
        return 1
    elif n>2:
        return fib(n-1)+fib(n-2)


for n in range(1,21):
    print(n, ":", fib(n))


#With Memoization technique
print("------------ Memoization ------------")

fib_cache = {}
def fib_memo(n):
    if n in fib_cache:
        print("print cache n:",n,"=> ",fib_cache[n])
        return fib_cache[n] 
    elif n == 1:
        value = 1
    elif n ==2:
        value = 1
    elif n>2:
        value = fib_memo(n-1)+fib_memo(n-2)
        
    fib_cache[n] = value
    return value

for n in range(1,31):
    print(n, ":", fib_memo(n))


#Python build-in LRU cache (Least Recently Used cache)
#By default @lru_cache Python will cache 128 most recent value cache

print("------------ LRU cache --------------")

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fib_lru(n):
    if n == 1:
        return 1
    elif n ==2:
        return 1
    elif n>2:
        return fib_lru(n-1)+fib_lru(n-2)

for n in range(1,21):
    print(n, ":", fib_lru(n))
