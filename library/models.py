from django.db import models

# Create your models here.

class Author(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    def __str__(self):
        return self.Name

class Book(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.ForeignKey(Author,on_delete=models.SET_NULL, null=True)
    Summary = models.TextField(max_length=500)
    Published_Date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Title
