from django.db import models

# Create your models here.

class Contact(models.Model):
    Title = models.CharField(blank=True, null=False, max_length=150)
    Post = models.CharField(blank=True, null=True, max_length=300)
    Height = models.IntegerField(blank=True, null=False)
    StateOfOrigin = models.CharField(blank=True, null=False,max_length=150)
    DateOfBirth = models.DateField(blank=True, null=False)

    @classmethod
    def __str__(self):
        return self.Title