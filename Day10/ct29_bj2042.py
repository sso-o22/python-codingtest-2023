# 백준 2042 - 구간 합 구하기 3 (세그먼트 트리)
import sys
input = sys.stdin.readline

# 수, 변경횟수, 구간합 횟수
N, M, K = map(int, input().split())
treeHeight = 0
length = N

while length != 0:
    length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 - 1
tree = [0] * (treeSize + 1)

# 데이터를 리프노드에 저장 / 8 ~ 13-1
for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + N + 1):
    tree[i] = int(input())

# 인덱스 트리
def setTree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1

setTree(treeSize - 1)

# 값 변경 함수
def changeVal(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + diff  # 차이값을 더함
        index = index // 2

# 구간핪 계산
def getSum(s, e):
    partSum = 0
    while s <= e:
        if s % 2 == 1:  # 시작값 독립노드 선택
            partSum += tree[s]
            s += 1
        if e % 2 == 0:  # 끝값 독립노드 선택
            partSum += tree[e]
            e -= 1
        s = s // 2
        e = e // 2
    return partSum

for _ in range(M + K):
    question, s, e = map(int, input().split())
    if question == 1:  # 값 변경
        changeVal(leftNodeStartIndex + s, e)
    elif question == 2:
        s = s + leftNodeStartIndex
        e = e + leftNodeStartIndex
        print(getSum(s, e))