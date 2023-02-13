# 입력속도를 개선! 단, 주피터노트북에서는 실행불가
import sys
input = sys.stdin.readline 

N, M = tuple(map(int, input().split()))
numbers = list(map(int, input().split()))
sums = [0]  # 핵심! 중요! 배열 0번째 인덱스
temp = 0

for i in numbers:
    temp = temp + i  # temp 5 9 12 14 15
    sums.append(temp)
    # [0, 5, 9, 12, 14, 15]

for i in range(M):
    x, y = tuple(map(int, input().split()))
    print(sums[y] - sums[x - 1])