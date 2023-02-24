def solution1(cards1, cards2, goal):
    answer = 'Yes'
    
    card1_sel, card2_sel = 0, 0  # 카드1,2 리스트에서 선택 카드
    
    # 카드리스트에서 꺼낸 값들을 목표 리스트 카드와 비교
    # 크기 비교는 횟수 때문
    for i in goal:  
        if len(cards1) > card1_sel and i == cards1[card1_sel]:
            card1_sel += 1  # 다음 카드 꺼내기
        elif len(cards2) > card2_sel and i == cards2[card2_sel]:
            card2_sel += 1  # 다음 카드 꺼내기
        else:
            answer = 'No'
            break
    return answer

cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solution1(cards1, cards2, goal)) # return Yes

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solution1(cards1, cards2, goal)) # return No