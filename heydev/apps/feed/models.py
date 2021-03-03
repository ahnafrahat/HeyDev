from django.db import models
from django.contrib.auth.models import User


class Hey(models.Model):
    body = models.CharField(max_length=225)

    created_by = models.ForeignKey(User, related_name='dev' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)