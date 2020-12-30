n,k = map(int, input().split())
result = 0

while True:
    if n % k == 0:
        n /= k
        result += 1
    else:
        n -= 1
        result += 1
    if n == 1:
        break

print(result)


n,k = map(int, input().split())
result = 0

while True:
    target

print(result)