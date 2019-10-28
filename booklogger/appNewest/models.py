from django.db import models

class Book(models.Model):
    bookTitle = models.CharField(max_length=256)
    bookAuthorFirstName = models.CharField(max_length=128)
    bookAuthorLastName = models.CharField(max_length=128)
    bookPrice = models.DecimalField(max_digits=8, decimal_places=2)
    bookGenre = models.CharField(max_length=128)
    bookAvailable = models.BooleanField(default=True)
    
