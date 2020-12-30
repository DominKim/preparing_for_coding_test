# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0

for _ in range(n):
    lst = list(map(int, input().split()))
    min_value = min(lst)
    result = max(min_value, result)

print(result)

# 2중 반복문 구조를 이용하는 답안 예시
n, m map(int, input().split())

result = 0
for _ in range(n):
    lst = list(map(int, input().split()))
    min_value = 1001
    for value in lst:
        min_value = min(min_value, value)
    reuslt = max(result, min_value)

print(reuslt)
