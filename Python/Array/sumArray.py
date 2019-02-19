#Sum array

#Solution 1
#Time complexity = O(N)
def sumArr1(n):

    result = 0
    for x in range(n+1):
        result += x
    print(result)
    return result

sumArr1(5)

#Solution 2, using Math formula
#Time complexity = O(1)
def sumArr2(n):

    return (n*(n+1)/2)

print(sumArr2(5))