from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(blank = "False")
    desc = models.CharField(max_length = 250)

    def __str__(self):
        return self.name 
