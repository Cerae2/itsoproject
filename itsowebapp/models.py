from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.name