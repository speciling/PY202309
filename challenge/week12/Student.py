class Student:
    # 속성 초기화
    name = ""
    korean, math, english = 0, 0, 0

    # 생성자(이름, 국어점수, 수학점수, 영어점수를 입력받아서 저장)
    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

    # 평균 반환 함수
    def get_average(self):
        return (self.korean + self.math + self.english) / 3