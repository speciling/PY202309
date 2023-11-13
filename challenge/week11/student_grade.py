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

def loadData(filename):
    fp = open(filename, "r", encoding="utf8")
    lines = fp.readlines()
    fp.close()
    student_list = []
    # lines의 두 번째 줄부터 각 줄을 line으로 가져옴
    for line in lines[1:]:
        # 각 줄을 , 기준으로 나눠서 맨 앞의 이름을 name에, 나머지 점수들을 scores 리스트에 저장
        name, *scores = line.strip().split(',')
        # 이름과, 점수의 리스트의 원소들을 float형으로 변환하여 언패킹한 점수들을 인자로 주어 Student 객체 생성
        student_list.append(Student(name, *map(float, scores)))
    return student_list


# TODO 1.1: 학생 정보를 리스트에 저장
try:
    student_list = loadData("./student.csv")

except FileNotFoundError:
    print("WARNING: 파일이 존재하지 않습니다. 파일명을 확인해주세요")    

else:
    # TODO 1.2: 학생 별 성적의 평균 점수를 출력
    # 평균 점수 정보를 저장할 리스트 선언
    average_score_data = ["-----학생들의 평균 점수------"]
    # student_list의 학생 객체들의 name 변수와 get_average 함수를 이용해 정해진 형식대로 점수 데이터 추가
    for student in student_list:
        average_score_data.append(f'{student.name}의 평균 점수는 {student.get_average()} 입니다.')
    # 각 줄을 출력
    print(*average_score_data, sep="\n")


    # TODO 1.3:  평균 점수를 코드 실행결과와 동일하게 파일로 출력 (average.txt)
    try:
        write_fp = open("average.txt", "w", encoding="utf8")
        # 점수 정보 리스트를 파일에 작성
        write_fp.write('\n'.join(average_score_data))
        write_fp.close()
    except:
        print("WARNING: 파일을 저장하는데 실패했습니다")