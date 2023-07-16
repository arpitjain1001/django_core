from django.contrib import admin
from django.db.models import Sum
from .models import *

# Register your models here.
from vege.models import receipe,StudentID,Student,Department,Subject,SubjectMarks,ReportCard

admin.site.register(receipe)

admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
# admin.site.register(ReportCard , ReportCardAdmin)
admin.site.register(Subject)


class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student' , 'subject' ,'marks']
admin.site.register(SubjectMarks)


def total_marks(self ,obj):
    subject_marks = SubjectMarks.objects.filter(student = obj.student)
    marks = (subject_marks.aggregate(marks = Sum('marks')))

    return marks['marks']

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student' , 'student_rank' ,'date_of_report_card_generation','total_marks']
    ordering = ['-student_rank']

admin.site.register(ReportCard , ReportCardAdmin)
