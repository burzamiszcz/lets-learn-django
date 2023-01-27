from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=50)

#     def __str__(self):
#         return self.username

class Ad(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    text = models.TextField(max_length=800)

    def __str__(self):
        return self.name

    def get_title(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    offer = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def get_message(self):
        return self.message_text