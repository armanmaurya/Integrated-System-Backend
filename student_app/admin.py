from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Course

class StudentAdmin(admin.ModelAdmin):
    using = 'default'  # PostgreSQL
    list_display = ('name','id', 'grade')  # Add the fields you want to display

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

admin.site.register(Student, StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    using = 'default'  # PostgreSQL
    list_display = ('id', 'name')  # Add the fields you want to display

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

admin.site.register(Course, CourseAdmin)
