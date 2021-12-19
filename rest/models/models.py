from django.db import models
from django.contrib.auth.models import UserManager


class Actor(models.Model):
    """俳優テーブル"""
    # actor_id = models.AutoField(primary_key=True)
    first_name = models.FileField(blank=True, max_length=45)
    last_name = models.FileField(blank=True, max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    class Meta:
        model = 'actor'
        fields = "__all__"
