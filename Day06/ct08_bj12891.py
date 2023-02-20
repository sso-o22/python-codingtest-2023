# 백준 12891 - DNA 비밀번호
checkList = [0] * 4  # ACGT 유전자값
myList = [0] * 4  # 부분 문자열의 ACGT 갯수
checkSecret = 0

# 함수
def myadd(c):  # 새로 들어온 문자를 처리
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c):  # 제거되는 문자를 처리
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret += 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret += 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret += 1
        myList[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

# print(S, P)
# print(Result)
# print(A)
# print(checkList)

for i in range(4):
    if checkList[i] == 0:  # ACGT 4
        checkSecret += 1  # 0없어도 되니까 처음부터 4로 맞추기위한 초기화

for i in range(P):  # 부분문자열 갯수만큼 2
    myadd(A[i])

if checkSecret == 4:  # ACGT / 4는 네자리 유전자 글자 다 조건만족
    Result += 1

for i in range(P, S):  # 2, 4
    j = i - P  # 0 - 2 == -2
    myadd(A[i])  # 이번 슬라이드에서 
    myremove(A[j])  # 이전 슬라이드에서 처리한 값을 제거
    if checkSecret == 4:
        Result += 1

print(Result)


'''
import sys
input = sys.stdin.readline

S,P = map(int, input().split())
A = list(map(str,input().rstrip()))
a,c,g,t = map(int, input().split())

result = 0

start = A[:P]
tmp = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}
for i in start:
    tmp[i] += 1

cnt = 0
if tmp["A"] >= a and tmp["C"] >= c and tmp["G"] >= g and tmp["T"] >= t:
    cnt += 1

start_idx = 0
end_idx = start_idx + P

for i in range(len(A)-P):
    tmp[A[start_idx+i]] -= 1 # 슬라이딩 : 1번째 데이터를 지우고
    tmp[A[end_idx+i]] += 1 # 마지막 데이터 추가하기
    if tmp["A"] >= a and tmp["C"] >= c and tmp["G"] >= g and tmp["T"] >= t:
        cnt +=1

print(cnt)
'''