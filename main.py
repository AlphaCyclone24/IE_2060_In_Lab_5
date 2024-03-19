class Student:
    HighestGPA = None

    def __init__(self, name, gpa, ch_completed):
        self.__name = name
        self.__gpa = gpa
        self.__ch_completed = ch_completed
        if Student.HighestGPA is None or gpa > Student.HighestGPA:
            Student.HighestGPA = gpa

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name

    @property
    def GPA(self):
        return self.__gpa

    @property
    def CHcompleted(self):
        return self.__ch_completed

    @property
    def Classification(self):
        if self.__ch_completed < 30:
            return 1
        elif self.__ch_completed < 60:
            return 2
        elif self.__ch_completed < 90:
            return 3
        else:
            return 4

    @staticmethod
    def Update(ch_course, grade):
        # Update CHcompleted
        self.__ch_completed += ch_course
        # Update GPA
        total_quality_points = self.__gpa * self.__ch_completed
        total_quality_points += grade * ch_course
        self.__gpa = total_quality_points / self.__ch_completed

        # Update HighestGPA if relevant
        if self.__gpa > Student.HighestGPA:
            Student.HighestGPA = self.__gpa

# Illustrating usage
if __name__ == "__main__":
    student1 = Student("Bob", 3.2, 45)
    print("Student Name:", student1.Name)
    print("Student GPA:", student1.GPA)
    print("Student Completed Credit Hours:", student1.CHcompleted)
    print("Student Classification:", student1.Classification)
    print("Highest GPA among students:", Student.HighestGPA)

    student2 = Student("John", 4.0, 60)
    print("\nStudent Name:", student2.Name)
    print("Student GPA:", student2.GPA)
    print("Student Completed Credit Hours:", student2.CHcompleted)
    print("Student Classification:", student2.Classification)
    print("Highest GPA among students:", Student.HighestGPA)
