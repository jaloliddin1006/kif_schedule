from django.contrib import admin
from .models import AboutFaculty, AboutDepartmentPeople, News, Students
# Register your models here.

admin.site.register(AboutFaculty)
admin.site.register(News)
admin.site.register(Students)

@admin.register(AboutDepartmentPeople)
class AboutDepartmentPeopleAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'department', 'position', 'place')
    list_filter = ('department',)
    search_fields = ('full_name', 'department', 'position',)