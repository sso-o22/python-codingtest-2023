# 프랙탈 원 그리기
import turtle  # 그림 그려주는 거북이

turtle.setup(width=600, height=600)
t = turtle.Turtle()  # 거북이 만들기
t.shape('turtle')

c = t.clone()  # 거북이 복제
c.color('green')
c.circle(30)

for i in range(4, 10):
    c.circle(i * 10)

turtle.mainloop()