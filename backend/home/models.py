from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class AboutFaculty(models.Model):
    image1 = models.ImageField(upload_to='about/')
    image2 = models.ImageField(upload_to='about/')
    image3 = models.ImageField(upload_to='about/')
    body = RichTextField()
    
    def __str__(self):
        return 'About Faculty'
    
class AboutDepartmentPeople(models.Model):
    image = models.ImageField(upload_to='dekanat/')
    place = models.IntegerField(default=1)
    body = RichTextField()
    
    def __str__(self):
        return self.body[:50]
    
    
class News(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news/')
    body = RichTextField()
    date = models.DateField()
    
    def __str__(self):
        return self.title[:50]
    
    