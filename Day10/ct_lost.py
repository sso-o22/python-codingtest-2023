def solution2(n, lost, reserve):
    answer = n - len(lost)  # 전체 학생수 - 잃어버린 학생수 = 수업들을 수 있는 학생수

    for i in lost:  # 잃어버린 리스트에서 돌기
        if i in reserve:  # 여분있는 리스트에서 돌기
            answer = answer + 1  # 수업들을 수 있는 학생수 증가
            reserve.remove(i)  # 여분에서 한명씩 지움
            continue

        # 앞 뒤 번호인지 확인
        for j in reserve:
            if j == i - 1:  # 여분학생이 잃어버린 학생보다 바로 앞이면
                answer = answer + 1  # 수업들을 수 있는 학생수 증가
                reserve.remove(j)  # 여분학생에서는 지우기
                break
            elif j == i + 1:  # 여분학생이 잃어버린 학생보다 바로 뒤면
                if j in lost:  # 근데 잃어버린 학생리스트에 있으면 빠져나감
                    break
                answer = answer + 1  # 아니면 수업들을 수 있는 학생수 증가
                reserve.remove(j)  # 여분학생에서는 지우기
                break

    return answer  # 수업들을 수 있는 학생수 반환

n = 5
lost = [2, 4]
reserve = [1,3,5]

print(solution2(n, lost, reserve)) # return 5


n = 5
lost = [2, 4]
reserve = [3]

print(solution2(n, lost, reserve)) # return 4


n = 3
lost = [3]
reserve = [1]

print(solution2(n, lost, reserve)) # return 2