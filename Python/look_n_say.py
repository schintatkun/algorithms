def next_number(n):
    result = []
    i = 0
    while i < len(n):
        count = 1
        while i + 1 < len(n) and n[i] == n[i+1]:
            i += 1
            count += 1
        result.append(str(count) + n[i])
        i += 1
    return ''.join(result)

start_term = "1"
n = 4

for i in range(n-1):
    start_term = next_number(start_term)
    print(start_term)
