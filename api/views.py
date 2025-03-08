from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from library_app.models import Book, IssuedBook
from library_app.serializer import BookSerializer, IssuedBookSerializer
from student_app.models import Student, Course
from student_app.serializer import StudentSerializer, CourseSerializer

book = Book.objects.using('library')
student = Student.objects.using('default')
issued_book = IssuedBook.objects.using('library')
course = Course.objects.using('default')

class QueryView(APIView):
    def get(self, request):
        grade = request.GET.get('grade')
        studentId = request.GET.get('studentid')
        name = request.GET.get('name')
        author = request.GET.get('author')
        status = request.GET.get('status')

        newData = []

        filters = {}
        if grade:
            filters['grade'] = grade
        if studentId:
            filters['id'] = studentId
        if name:
            filters['name__icontains'] = name  # Use __icontains for case-insensitive search

        result = student.filter(**filters)
        serializer = StudentSerializer(result, many=True)

        data = serializer.data
        for sutdent in data:
            issued_books_filters = {'student_id': sutdent['id']}
            if author:
                issued_books_filters['book__author__icontains'] = author  # Filter by author if given
            if status:
                issued_books_filters['status'] = status  # Filter by status if given

            issued_books = issued_book.filter(**issued_books_filters)
            books = addIssuedBook(issued_books)
            sutdent['issued_books'] = books
            if issued_books.count() != 0:
                newData.append(sutdent)

        return Response(newData)

def addIssuedBook(issued_books):
    books = []

    for book in issued_books:
        book_data = book.book
        book_serializer = BookSerializer(book_data)
        books.append(book_serializer.data)

    return books

class BookView(APIView):
    def get(self, request):
        query = request.GET.get('q')

        result = book.get(id=query)
        serializer = BookSerializer(result)
        return Response(serializer.data)
