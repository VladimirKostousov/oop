class Mentor:
    '''класс менторов'''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


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

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Git']

cool_mentor.rate_hw(best_student, 'Python', 1)
cool_mentor.rate_hw(best_student, 'Python', 5)
cool_mentor.rate_hw(best_student, 'Python', 5)

cool_mentor.rate_hw(best_student, 'Git', 5)
cool_mentor.rate_hw(best_student, 'Git', 5)
cool_mentor.rate_hw(best_student, 'Git', 5)

best_lecture = Lecture('Ivan', 'Fedorov')
best_lecture.courses_attached += ['Python']

best_student.rate_lecture(best_lecture, 'Python', 10)
best_student.rate_lecture(best_lecture, 'Python', 9)
best_student.rate_lecture(best_lecture, 'Python', 10)

some_reviewer = cool_mentor
some_lecturer = best_lecture
some_student = best_student
print(some_reviewer)
print(some_lecturer)
print(best_student)