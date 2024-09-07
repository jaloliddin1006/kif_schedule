from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
    

class AboutFaculty(models.Model):
    title = models.CharField(max_length=250, null=True)
    image1 = models.ImageField(upload_to='about/')
    image2 = models.ImageField(upload_to='about/')
    image3 = models.ImageField(upload_to='about/')
    body = RichTextField()
    
    def __str__(self):
        return 'About Faculty'
    
class AboutDepartmentPeople(models.Model):
    STAFF_CHOICES = (
    ('dekanat', 'Dekanat'),
    ('kafedra', 'Kafedra'),
    ('tutor', 'Tyutor'),
    )
    full_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='dekanat/')
    department = models.CharField(max_length=150, choices=STAFF_CHOICES)
    position = models.CharField(max_length=150)
    reception_time = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    place = models.IntegerField(default=1)
    
    def __str__(self):
        return self.full_name
    
    
class News(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news/')
    body = RichTextField()
    date = models.DateField()
    
    def __str__(self):
        return self.title[:50]
    
    
class Students(models.Model):
    image = models.ImageField(upload_to='students/')
    body = RichTextField()
    
    def __str__(self):
        return self.body[:50]