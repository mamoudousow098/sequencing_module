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