from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to='images/')
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
    