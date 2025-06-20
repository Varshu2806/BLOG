from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Summary(models.Model):
    title=models.CharField(max_lenghth=250)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
