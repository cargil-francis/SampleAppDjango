from django.db import models

# Create your models here.
class Author(models.Model):
    Name=models.CharField(max_length=250)
    Age=models.IntegerField(null=True)

class Book(models.Model):
    Title= models.CharField(max_length=250)
    Author=models.ForeignKey(Author,on_delete=models.CASCADE)
    Summary=models.TextField()
    Published_date=models.DateField()



   

    





