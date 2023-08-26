from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(null=True)



    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text