from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Ad(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    text = models.CharField(max_length=800)

    def __str__(self):
        return self.name