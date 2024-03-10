from django.urls import path
from .views import AboutFacultyView, DekanatView, NewsView, DetailView, StudentsView, ScheduleView

urlpatterns = [
    path('', AboutFacultyView.as_view(), name='about'),
    path('dekanat/', DekanatView.as_view(), name='dekanat'),
    path('news/', NewsView.as_view(), name='news'),
    path('detail/<int:id>/', DetailView.as_view(), name='detail'),
    path('students/', StudentsView.as_view(), name='students'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    
]