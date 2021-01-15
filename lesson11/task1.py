class Person:

    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age


class Teacher(Person):
    salary_coefficient = 0.1

    def __init__(self, name, surname, gender, age, subject, salary, lenth_of_service):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.lenth_of_service = lenth_of_service
        self.subject = subject
        self.salary = salary

    def represent_teacher(self):
        full_name = self.name + ' ' + self.surname
        return '{} is a teacher of the year!!!'.format(full_name)

    def annual_recount(self, lenth):
        current_coef = lenth*Teacher.salary_coefficient
        return 'initial salary is {} \ncurrent salary is {} thousands for year'.format(self.salary, current_coef*self.salary+self.salary)




class Student(Person):
    SUBJECTS = {'mathematics':[], 'biology':[], 'physics':[], 'chemistry':[]}
    MATH = []
    BIO = []
    PHYS = []
    CHEM = []


    def __init__(self, name, surname, gender, age, grade):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.grade = grade



    def represent_student(self):
        return ' {} {} is {} years old.'.format(self.name, self.surname, self.age)

    def grade_info(self):
        full_name = self.name + ' ' + self.surname
        return 'student {} goes to {} grade'.format(full_name, self.grade)

    def middle_mark(self, math_mark, bio_mark, phys_mark, chem_mark):
        marks = [math_mark, bio_mark, phys_mark, chem_mark]
        return sum(marks)/4

    def mark_list(self, subject, *mark):
        Student.SUBJECTS[subject] = mark
        return Student.SUBJECTS


pupil1 = Student('Mark', 'Knopfler', 'male', '9', 'second')
print(pupil1.represent_student())
print(pupil1.grade_info())
print(pupil1.middle_mark(5,3,2,3))

teacher1 = Teacher('James', 'Hatfield', 'male', 30, 'math', 100, 5)
print(teacher1.represent_teacher())
print(teacher1.annual_recount(2))
print(pupil1.mark_list('mathematics', 3,5))
print(pupil1.mark_list('biology', 3,5,4,5))
print(pupil1.mark_list('physics', 3,5,5))
print(pupil1.mark_list('chemistry', 5,4,5))
