class student:    # 학생 클래스의 정의

    def __init__(self, name, age, score):  # 학생들의 클래스 이름 나이 점수를 초기 값을 설정
        self.name = name     # 이름
        self.age = age  # 나이
        self.score = score  # 점수

    def display(self):
        print(f"이름: {self.name}, 나이: {self.age}, 점수: {self.score}") # 학생의 정보를 출력하는 메소드 

student_list = []   # 리스트 생성

student1 = student("정은호", 28, 90)  # 학생 1의 정보1
student2 = student("김기웅", 28, 85)  # 학생 2의 정보2
student3 = student("김시윤", 28, 80)  # 학생 3의 정보3

student_list.append(student1) #학생 1을 리스트에 추가 코드
student_list.append(student2) #학생 2를 리스트에 추가 코드
student_list.append(student3) #학생 3을 리스트에 추가 코드

for student in student_list:  # 반복문
    student.display()   #각 학생 정보 출력
