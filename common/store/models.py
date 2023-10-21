from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    info = models.TextField(blank=True) 
    price = models.IntegerField(
        validators=[
            MaxValueValidator(100_000_000),
            MinValueValidator(0) 
        ]
    ) 

    def __str__(self) -> str:
        return self.title 
        


class Category(models.Model):
    title = models.CharField(max_length=150) 

    def __str__(self) -> str:
        return self.title