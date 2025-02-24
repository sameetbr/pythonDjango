from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False) #Bir şey girmemz zorunlu hale geldi
    date = models.DateField()
    isActive = models.BooleanField()

    def __str__(self):
        return f"{self.title} {self.date}"