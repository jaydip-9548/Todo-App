from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=50)
    description = models.CharField(max_length=200,default = "")
    completed = models.BooleanField(default=False);
