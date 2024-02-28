from django.contrib import admin
from .models import AboutFaculty, AboutDepartmentPeople, News
# Register your models here.

admin.site.register(AboutFaculty)
admin.site.register(AboutDepartmentPeople)
admin.site.register(News)