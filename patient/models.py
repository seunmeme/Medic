from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


GENDER_CHOICES = [
                    ('MALE', 'Male'),
                    ('FEMALE', 'Female')
                ]  

class Record(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    telephone = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='MALE')
    address = models.TextField()
    condition = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.condition

    def get_absolute_url(self):
        return reverse('record_detail', kwargs={'pk':self.pk})


