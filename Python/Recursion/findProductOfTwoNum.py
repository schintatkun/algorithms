# Given 2 numbers, find their product using recursion
 
x = 9
y = 4
# concept of multiply
# 9 x 4 => 9+9+9+9

def findProduct_two_num(a, b):
    # Base case
    # optional to prevent runtime error, which caused by max recursive call exceeded.
    if b > a:
        return findProduct_two_num(b, a)

    #  b = 0 is when recursive call stop
    if b == 0:
        return 0
    else:
        return a+ findProduct_two_num(a, b-1)


print(findProduct_two_num(x,y))