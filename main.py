class Mentor:
    '''класс менторов'''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Student:
    ''' класс студентов'''
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grades(self):
        all_grades = sum(self.grades.values(), [])
        average = round(sum(all_grades) / len(all_grades), 2)
        return average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не корректные данные!')
            return
        return self._average_grades() < other._average_grades()

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n'
                  f'Средняя оценка за домашние задания: {self._average_grades()}\n'
                  f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                  f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return result


class Lecture(Mentor):
    '''класс лекторов'''
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grades(self):
        all_grades = sum(self.grades.values(), [])
        average_grades = round(sum(all_grades) / len(all_grades), 2)
        return average_grades

    def __lt__(self, other):
        if not isinstance(other, Lecture):
            print('Не корректные данные!')
            return
        return self._average_grades() < other._average_grades()

    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self._average_grades()}')
        return res


class Reviewer(Mentor):
    '''класс экспертов, проверяющих домашнее задание'''
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Paul', 'Henderson', 'male')
student_2.courses_in_progress += ['Python', 'Git', 'JavaScript']
student_2.finished_courses += ['Введение в программирование']

mentor_1 = Mentor('Some', 'Buddy')
mentor_1.courses_attached += ['Python', 'Git']
mentor_2 = Mentor('John', 'Cena')
mentor_2.courses_attached += ['Python', 'Git', 'JavaScript']

lecture_1 = Lecture('Severus', 'Snape')
lecture_1.courses_attached += ['Python', 'Git']
lecture_2 = Lecture('Salazar', 'Slytherin')
lecture_2.courses_attached += ['Python', 'Git', 'JavaScript', 'Parseltongue']

reviewer_1 = Reviewer('Lionel', 'Messi')
reviewer_1.courses_attached += ['Python', 'Git', 'How to win world cup']
reviewer_2 = Reviewer('Cristiano', 'Ronaldo')
reviewer_2.courses_attached += ['Python', 'Git', 'JavaScript']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Git', 10)

student_1.rate_lecture(lecture_1, 'Python', 10)
student_2.rate_lecture(lecture_2, 'Git', 9)
student_1.rate_lecture(lecture_1, 'Python', 5)
student_2.rate_lecture(lecture_2, 'Git', 10)

print(student_1)
print(student_2)
print(lecture_1)
print(lecture_2)
print(reviewer_1)
print(reviewer_2)
print(student_1 > student_2)
print(lecture_1 < lecture_2)

stud = [student_1, student_2]
lector = [lecture_1, lecture_2]


def mean_students(students, course):
    all_grades_students = []
    for student in students:
        all_grades_students += student.grades.get(course)
    mean_grade = round(sum(all_grades_students) / len(all_grades_students), 2)
    return mean_grade


def mean_lecturers(lecturers, course):
    all_grades_lecturers = []
    for lecture in lecturers:
        all_grades_lecturers += lecture.grades.get(course, [])
    mean_grades = round(sum(all_grades_lecturers) / len(all_grades_lecturers), 2)
    return mean_grades


print(mean_students(stud, 'Python'))
print(mean_lecturers(lector, 'Python'))