**클래스로 학생 리스트 만들기**
```class student:    # 학생 클래스의 정의로 시작

  def __init__(self, name, age, score):  # 학생들의 클래스 이름 나이 점수를 초기 값을 설정
    self.name = name     # 이름
    self.age = age  # 나이
    self.score = score  # 점수

  def displat(self):
    printf"이름: {self.name}, 나이: {self.age}, 점수: {self.score}")  # 학생들의 정보 출력 메소드 입력

student_list = []  #리스트 생성 

student1 = student("정은호", 28, 90)   # 이름 , 나이 , 점수 순으로 학생 1의 정보를 나열
student2 = student("김기웅", 28, 85)   # 이름 , 나이 , 점수 순으로 학생 2의 정보를 나열
student3 = student("김시윤", 28, 80)   # 이름 , 나이 , 점수 순으로 학생 3의 정보를 나열

student_list.append(student1) #학생 1을 리스트에 추가
student_list.append(student2) #학생 2을 리스트에 추가
student_list.append(student3) #학생 3을 리스트에 추가

for studen in student_list:  # 반복문
  student.displat()  # 각 학생들읠 정보 출력
```


**터미널 실행**<br>
python lest_class.py


**결과값**<br>
이름: 정은호, 나이: 28, 점수: 90<br>
이름: 김기웅, 나이: 28, 점수: 85<br>
이름: 김시윤, 나이: 28, 점수: 80

<img width="468" height="73" alt="list_class_결과값" src="https://github.com/user-attachments/assets/efaa81f7-624a-4e4a-beec-98415cd18e5d" /> <br>

