from django.shortcuts import render
from .models import AboutFaculty, AboutDepartmentPeople, News, Students 
from django.views import View
# Create your views here.


class AboutFacultyView(View):
    def get(self, request):
        about = AboutFaculty.objects.first()
        return render(request, 'index.html', {'about': about})
    
    
class DekanatView(View):
    def get(self, request):
        dekanat = AboutDepartmentPeople.objects.all().order_by('place')
        return render(request, 'administration.html', {'dekanat': dekanat})

class StudentsView(View):
    def get(self, request):
        students = Students.objects.all()
        return render(request, 'students.html', {'students': students})
    
class ScheduleView(View):
    def get(self, request):
        return render(request, 'schedule.html') 
    
       
class NewsView(View):
    def get(self, request):
        news = News.objects.all().order_by('-id')[:5]
        return render(request, 'news.html', {'news': news})
        
class DetailView(View):
    def get(self, request, id):
        new = News.objects.get(id=id)
        return render(request, 'detail.html', {'new': new})