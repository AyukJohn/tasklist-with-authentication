from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, null=True,on_delete= models.CASCADE, blank=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering=['complete']