from django.db import models

# creating model for creating department
class CreateLeaveInfo(models.Model):
   
    leavefrom = models.DateField()
    leavetill = models.DateField()
    leavetype = models.CharField(max_length=50)
    leavedesc = models.TextField()

    