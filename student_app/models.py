from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    grade = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    class Meta:
        app_label = 'student_app'  # Ensure it uses the student database

    def __str__(self):
        return self.name
    

































    
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.CharField(max_length=100)

    class Meta:
        app_label = 'student_app'  # Ensure it uses the student database
