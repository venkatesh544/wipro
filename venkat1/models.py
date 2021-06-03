from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class venkat1(models.Model):
    userid = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=16)
    dateofjoining = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userid