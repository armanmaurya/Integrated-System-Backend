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
        book = request.GET.get('book')
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
            if book:
                issued_books_filters['book__title__icontains'] = book  # Filter by author if given
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

class StudentNameView(APIView):
    def get(self, request):
        result = student.all()
        serializer = StudentSerializer(result, many=True)

        data = serializer.data
        names = set([student['name'] for student in data])
        return Response(names)

class BookView(APIView):
    def get(self, request):
        # Get All Books in array
        result = book.all()
        serializer = BookSerializer(result, many=True)

        # Construct Array of Names
        data = serializer.data

        names = set([book['title'] for book in data])
        return Response(names)
    

# class AuthorView(APIView):
#     def get(self, request):
#         result = book.all()
#         # Get all the authors
#         authors = set([book.author for book in result])

#         return Response(authors)
