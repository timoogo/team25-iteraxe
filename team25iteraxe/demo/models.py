from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Subject(models.Model):
    matricule = models.CharField(max_length=200, default=None, null=None)
    name = models.CharField(max_length=200, default=None, null=None)
    first_name = models.CharField(max_length=200, default=None, null=None)
    description = models.CharField(max_length=3000, null=True)
    first_day = models.DateTimeField(default=timezone.now)
    is_dead = models.BooleanField(default=False)
    virus_name_test = models.CharField(max_length=200, default=None, null=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'Matricule:{self.matricule}, Name: {self.first_name, self.name} '
