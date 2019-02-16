
# Sigma(5) = 1+2+3+4+5 = 15
# Sigma(4) = 1+2+3+4 = 10
# Sigma(3) = 1+2+3 = 6
# Sigma(2) = 1+2 = 3
# Sigmm(1) = 1 

# Time O(n)

def sigma(n):
    if n < 0 :
        return 0
    else: 
        return sigma(n-1)+n

print(sigma(5))
print(sigma(20))