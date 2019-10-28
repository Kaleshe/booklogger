from django.db import models

# Create your models here.


class Book(models.Model):
   bookAuthor = models.CharField(max_length=128, default='a')
   bookCat = models.CharField(max_length=64, default='a')
   bookPblshr = models.CharField(max_length=128, default='a')

   bookTitle = models.CharField(max_length=128, default='a')
   bookDsc = models.TextField(max_length=1000, default='a')
   bookImg = models.ImageField(upload_to='pics')
   bookPrice = models.DecimalField(max_digits=8 ,decimal_places=2, default=0.00)
   bookISBN = models.BigIntegerField(default=11111)
   bookPages = models.PositiveIntegerField(default=1)

   LANGS = [
    ('ENG', 'English'),
    ('GER', 'German'),
    ('ESP', 'Spanish')]
   bookLang = models.CharField(max_length=3, choices=LANGS, default='EN')


   bookSale = models.BooleanField(default=False)
   bookFreeShip = models.BooleanField(default=False)
