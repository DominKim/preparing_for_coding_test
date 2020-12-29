# sorted
result = sorted([9, 1, 8, 5, 4])
print(result)

# sorted with key
array = [("홍길동", 35), ("이순신", 75), ("아무개", 59)]
result = sorted(array, key = lambda x: x[1], reverse=True)
print(result)

# 순열 
from itertools import permutations, combinations

data  = ["A", "B", "C"]

result = list(permutations(data, 3))
print(result)

# 횟수
from collections import Counter

counter = Counter(["red", "blue", "red", "green", "blue", "blue"])
print(counter["red"])
print(dict(counter))

# 최대 공약수
import math
# 최소 공배수를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14))
print(lcm(21, 14))