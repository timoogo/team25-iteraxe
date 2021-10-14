from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Subject(models.Model):
    first_name = models.CharField(max_length=200, default=None, null=None)
    last_name = models.CharField(max_length=200, default=None, null=None)
    matricule = models.CharField(max_length=200, default=None, null=None)
    description = models.CharField(max_length=3000, null=True)
    first_day = models.DateTimeField(default=timezone.now)
    state = models.IntegerField(validators=[MinValueValidator(-1), MaxValueValidator(1)], default=0)
    image = models.ImageField(upload_to='subjects_images', default=None, null=None)
    virus_name = models.CharField(max_length=200, default=None, null=None)
    cure = models.CharField(max_length=200, default=None, null=None)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'Matricule:{self.matricule}, Name: {self.first_name, self.last_name} '

class Guard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=200, default="SDR", null=None)
