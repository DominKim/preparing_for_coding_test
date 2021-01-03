'''
행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
나이트는 매우 충성스러운 신하로서 매일 무술을 연마한다.
나이트는 마을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

'''

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord("a")) + 1

steps = [(-2, -1), (2, -1), (-2, 1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)