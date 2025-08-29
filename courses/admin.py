from django.contrib import admin
from .models import Course, Enrollment, Lesson

# Register your models here.
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Lesson)