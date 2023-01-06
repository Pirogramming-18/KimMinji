##############  예외 만들기
class NumOfDataError(Exception):
    def __init__(self):
        super().__init__("Num of data is not 3!")
class ExistNameError(Exception):
    def __init__(self):
        super().__init__("Already exist name!")
class NotPositiveIntegerError(Exception):
    def __init__(self):
        super().__init__("Score is not positive integer!")
class NoStudentDataError(Exception):
    def __init__(self):
        super().__init__("No student data!")
class NoStudentWithoutGradeError(Exception):
    def __init__(self):
        super().__init__("No student without grade!")
class NeedGradingError(Exception):
    def __init__(self):
        super().__init__("There is a student who didn't get grade")
class NotExistNameError(Exception):
    def __init__(self):
        super().__init__("Not exist name!")

##############  빈 학생 정보 list
studentsInfo = []

##############  menu 1
def Menu1() :
    studentsInfo.append(list(studentInfo))

##############  menu 2
def Menu2() :
    m = 0
    for i in range(len(studentsInfo)):
        if len(studentsInfo[m]) == 3:
            average = (int(studentsInfo[m][1]) + int(studentsInfo[m][2])) / 2
            if average >= 90:
                grade = "A"
            elif 80 <= average < 90:
                grade = "B"
            elif 70 <= average < 80:
                grade = "C"
            else:
                grade = "D"
            studentsInfo[m].append(grade)
        m += 1

##############  menu 3
def Menu3() :
    print("\n--------------------------")
    print("name     mid  final  grade")
    print("--------------------------")
    m = 0
    for i in range(len(studentsInfo)):
        print(studentsInfo[m][0].ljust(8), str(studentsInfo[m][1]).rjust(3), str(studentsInfo[m][2]).rjust(5), studentsInfo[m][3].rjust(5))
        m += 1

##############  menu 4
def Menu4():
    del studentsInfo[deleteIndex]

##############  출력 시작
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    
##############  1번 선택
    if choice == "1" :
        n = 0
        checkName = 0
        try:
            studentInfo = list(input("Enter name mid-score final-score : ").split())
            if len(studentInfo) != 3:
                raise NumOfDataError
            elif len(studentInfo) == 3:
                for i in range (len(studentsInfo)):
                    if studentInfo[0] == studentsInfo[n][0]:
                        checkName += 1
                    n += 1
                try:
                    if checkName >= 1:
                        raise ExistNameError
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        else:
            try:
                if studentInfo[1].isdigit() == False or studentInfo[2].isdigit() == False:
                    raise NotPositiveIntegerError
            except Exception as e:
                print(e)
            else:
                Menu1()
                
##############  2번 선택
    elif choice == "2" :
        n = 0
        checkGrade = 0
        for i in range(len(studentsInfo)):
            if len(studentsInfo[n]) == 3:
                checkGrade += 1
            n =+ 1
        try:
            if len(studentsInfo) == 0:
                raise NoStudentDataError
            elif checkGrade == 0:
                raise NoStudentWithoutGradeError
        except Exception as e:
            print(e)
        else:
            print("Grading to all students.")
            Menu2()

##############  3번 선택
    elif choice == "3" :
        n = 0
        checkGrade = 0
        for i in range(len(studentsInfo)):
            if len(studentsInfo[n]) == 3:
                checkGrade += 1
            n =+ 1
        try:
            if len(studentsInfo) == 0:
                raise NoStudentDataError
            elif checkGrade >= 1:
                raise NeedGradingError
        except Exception as e:
            print(e)
        else:
            Menu3()

##############  4번 선택
    elif choice == "4" :
        checkName = 0
        deleteIndex = 0
        n = 0
        try:
            if len(studentsInfo) == 0:
                raise NoStudentDataError

            elif len(studentsInfo) != 0:
                deleteName = input("Enter the name to delete : ")
                for i in range(len(studentsInfo)):
                    if deleteName == studentsInfo[n][0]:
                        deleteIndex = n
                        checkName += 1
                    n += 1
                try:
                    if checkName == 0:
                        raise NotExistNameError
                except Exception as e:
                    print(e)
                else:
                    Menu4()
                    print(deleteName, "student information is deleted.")
        except Exception as e:
            print(e)

##############  5번 선택
    elif choice == "5" :
        print("Exit Program!")
        break
    
##############  잘못 선택
    else :
        print("Wrong number. Choose again.")