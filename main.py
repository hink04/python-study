from student import Student


students = []

while True:

    print("\n1. 학생 추가")
    print("2. 학생 보기")
    print("3. 종료")

    choice = input("선택: ")

    if choice == "1":
        name = input("이름: ")
        score = int(input("점수: "))

        student = Student(name, score)
        students.append(student)

        print("추가 완료")

    elif choice == "2":
        for s in students:
            s.show()

    elif choice == "3":
        break