from django.urls import path
from .views import AboutFacultyView, DekanatView, NewsView, DetailView

urlpatterns = [
    path('', AboutFacultyView.as_view(), name='about'),
    path('dekanat/', DekanatView.as_view(), name='dekanat'),
    path('news/', NewsView.as_view(), name='news'),
    path('detail/<int:id>/', DetailView.as_view(), name='detail'),
    
]