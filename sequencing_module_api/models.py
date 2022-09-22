from ipaddress import ip_address
from django.db import models

# Create your models here.


class User(models.Model):
    id_user=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = "User"



class Ordinateur(models.Model) :
    hostname=models.CharField(max_length=255, primary_key=True)
    ip_address=models.CharField(max_length=100)
    user=models.CharField(max_length=100)
    password=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.hostname + " ip : " + self.ip_address

    class Meta :
        db_table = "Ordinateur"
