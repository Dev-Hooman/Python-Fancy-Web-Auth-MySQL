from django.db import models

# Create your models here.
class users(models.Model):
    user_name = models.CharField(max_length=50, null=False)
    user_email = models.EmailField(max_length=70, null=False)
    user_password = models.CharField(max_length=50, null=False)
    user_gender = models.CharField(max_length=10, null=False)
    user_DOB = models.DateField()
    user_phoneNumber = models.IntegerField()
    user_address = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name






