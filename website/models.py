from django.db import models
from django.db import models

class Main(models.Model):

    name = models.TextField(max_length=30)
    about = models.TextField(max_length=450)
    about2 = models.TextField(max_length=450)
    fb = models.TextField(default="-")
    tw = models.TextField(default="-")
    yt = models.TextField(default="-")
    ig = models.TextField(default="-")

    def __str__(self):
        return self.about
# Create your models here.



