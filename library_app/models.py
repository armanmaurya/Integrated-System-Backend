from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    available_copies = models.IntegerField()

    class Meta:
        app_label = 'library_app'

    def __str__(self):
        return self.title

class IssuedBook(models.Model):
    STATUS_CHOICES = [
        ('Returned', 'Returned'),
        ('Non Returned', 'Non Returned'),
    ]

    issued_date = models.DateField()
    student_id = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    class Meta:
        app_label = 'library_app'

    def __str__(self):
        return self.book.title