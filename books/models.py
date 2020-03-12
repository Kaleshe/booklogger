from django.db import models
from djmoney.models.fields import MoneyField
from mptt.managers import TreeManager
from mptt.models import MPTTModel

class Author(models.Model):
   autFirstN = models.CharField(max_length=64)
   autMidN = models.CharField(max_length=64)
   autLastN = models.CharField(max_length=64)

   def __str__(self):
      return self.autLastN

class Book(models.Model):
   bookAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
#  bookCat = models.ForeignKey(Category, related_name="books", on_delete=models.CASCADE)
#  bookPblshr = models.ForeignKey(Publisher, on_delete=models.CASCADE)

   bookTitle = models.CharField(max_length=128)
   bookDsc = models.TextField(max_length=1000)
   bookImg = models.ImageField(upload_to='pics')
   bookPrice = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='EUR')
   bookISBN = models.BigIntegerField(default=11111)
   bookPages = models.PositiveIntegerField(default=10)

   LANGS = [
    ('ENG', 'English'),
    ('GER', 'German'),
    ('ESP', 'Spanish')]
   bookLang = models.CharField(max_length=3, choices=LANGS, default='ENG')

   bookSale = models.BooleanField(default=False)
   bookFreeShip = models.BooleanField(default=False)

   def __str__(self):
      return self.bookTitle
