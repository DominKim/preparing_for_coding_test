# 거스름돈
money = 1260
cnt = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    cnt += money // coin
    money %= coin

print(cnt)

# # 큰수의 법칙

# # N, M, K를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())
# # n개의 수를 공백으로 구분하여 비력받기
# data = list(map(int, input().split()))

# data.sort()
# first = data[n - 1]
# second = data[n - 2]

# result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1

# print(result)


n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 비력받기
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

if m % (k + 1) == 0:
    count = (m //(k + 1)) * k
else:
    count = (m // (k + 1)) * k + m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)