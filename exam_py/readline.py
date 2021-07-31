
import sys
#문자열 입력받기
data = sys.stdin.readline().rstrip()
#rstrip는 readlin() 엔터가 줄 바꿈 기호로 변경되기때문에 공백 문자르 제거하기 위해 사용한 함수

print(data)


#출력할 변수들
a = 1
b = 2
print(a, b)
print(7, end="") #출력할때의 자동 띄어쓰기를 없앤 end함수
print(8, end="")

#출력할 변수
answer = 7
print("정답은" + str(answer) + "입니다.")

#or

print(f"정답은 {answer}입니다.")

#or

print("정답은", answer, "입니다.")