from django.db import models
# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=264)
    email=models.EmailField(unique=True)
    v_mail=models.EmailField()
    feedback=models.CharField(max_length=264)
    def __str__(self):
        return self.name
