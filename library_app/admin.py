from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book, IssuedBook

class BookAdmin(admin.ModelAdmin):
    using = 'library'  # SQLite

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

admin.site.register(Book, BookAdmin)


class IssuedBookAdmin(admin.ModelAdmin):
    using = 'library'  # SQLite

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)
    
admin.site.register(IssuedBook, IssuedBookAdmin)
