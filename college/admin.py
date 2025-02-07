from django.contrib import admin
from college.models import Notice, Student
# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['subject', 'cr_date', 'msg']
    search_fields = ['subject', 'msg']
    list_filter = ['cr_date']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    search_fields = ['name', 'address']
    list_filter = ['address']
    

    
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Student, StudentAdmin)
