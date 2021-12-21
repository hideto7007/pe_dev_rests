from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth import get_user_model


class Actor(models.Model):
    """俳優テーブル"""
    actor_id = models.AutoField(primary_key=True)
    first_name = models.FileField(blank=True, max_length=45)
    last_name = models.FileField(blank=True, max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class JobOffer(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    salary = models.PositiveSmallIntegerField()
    prefectures = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.company_name
