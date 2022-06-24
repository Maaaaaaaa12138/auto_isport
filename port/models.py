from django.db import models

class JSESSIONID(models.Model):    

    content = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default="isport")

class Status(models.Model):
    content = models.CharField(max_length=255)
    time = models.DateField()

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"{self.time}-{self.content}"
