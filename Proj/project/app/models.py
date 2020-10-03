from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length = 122)
    lname = models.CharField(max_length = 122)
    email = models.EmailField(max_length = 122)
    phone = models.IntegerField
    comment = models.TextField()
    date = models.DateTimeField()   

    def __str__(self):
        return self.fname
