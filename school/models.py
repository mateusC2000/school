from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length = 14)

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    code = models.CharField(max_length = 10)
    description = models.CharField(max_length = 100, blank = False)
    level = models.CharField(max_length = 1, choices = LEVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.code

class Registration(models.Model):
    PERIOD = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    period = models.CharField(max_length = 1, choices = PERIOD, blank = False, null = False, default = 'M')
    