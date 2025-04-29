BAR_WIDTH = 25

class Student(object):
    """A class that models a student, with a name, numeric identifier, and mark."""

    def __init__(self, name:str, id_num:str, mark:float) -> None:
        self.__name = name
        self.__id_num = id_num
        self.__mark = mark

    def get_name(self) -> str:
        """Accessor for the student's name."""
        return self.__name

    def get_id_num(self) -> int:
        """Accessor for the student's numeric identifier."""
        return self.__id_num

    def get_mark(self) -> float:
        """Accessor for the student's mark."""
        return self.__mark

    def set_mark(self, mark:float) -> None:
        """Mutator for the student's mark."""
        self.__mark = mark

    def __radd__(self, student) -> int:
        # implemented to get sum() working
        mark = student
        if type(student) == Student:
            mark = student.get_mark()
        return self.__mark + mark

    def __lt__(self, student) -> bool:
        return self.__mark < student.get_mark()

class Course_Section(object):
    """A class that models a course section, with a course code, section number, and a list of students."""

    def __init__(self, course_code:str, section_number:int, students:list[Student]=[]) -> None:
        self.__course_code = course_code
        self.__section_number = section_number
        self.__students = students

    def add_student(self, student:Student) -> None:
        """Adds a student to the private list of students."""
        self.__students.append(student)

    def remove_student(self, id_num:str) -> None:
        """Adds a student to the private list of students."""
        self.__students.remove(self.get_student(id_num))

    def get_student(self, id_num:str) -> Student:
        student = None

        i = 0
        while not student and i < len(self.__students):
            if self.__students[i].get_id_num() == id_num:
                student = self.__students[i]
            i += 1

        return student

    def num_students(self) -> int:
        return len(self.__students)

    def get_average(self) -> float:
        return sum(self.__students) / len(self.__students)

    def update_mark(self, id_num:str, mark:float) -> None:
        self.get_student(id_num).set_mark(mark)

    def __str__(self) -> str:
        return "" # to implement

    def top_student(self) -> Student:
        return max(self.__students)

if __name__ == "__main__":
    f = open("student_data.txt")
    course = Course_Section("ICS4U", 1)
    print("-" * BAR_WIDTH)
    
    for line in f:
        line = line.strip().split(",")

        name = line[0]
        idnum = line[1]
        mark = float(line[2])

        stud = Student(name, idnum, mark)
        course.add_student(stud)

    print("> Adding back last student...")
    course.add_student(stud)
    print("-" * BAR_WIDTH)

    print("> Removing last student...")
    course.remove_student(idnum)
    print("-" * BAR_WIDTH)
    
    print(f"> Giving last student a {mark:.0f}% [unchanged]...")
    course.update_mark(idnum, mark)
    print("-" * BAR_WIDTH)

    print("> Outputting student data...")
    print(f"\t# of students: {course.num_students()}")
    print(f"\tAverage: {course.get_average():.2f}")
    print(f"\tTop student: {course.top_student().get_name()}")
    print("-" * BAR_WIDTH)

    print(course)
    print("-" * BAR_WIDTH)
