
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    id_user=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, unique=True)
    password = models.CharField(max_length=255, null=True)
    fonction = models.CharField(max_length=255, null=True)
    groups = None
    user_permissions = None
    

    
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = "user"



class Sequenceur(models.Model) :
    hostname=models.CharField(max_length=255, primary_key=True)
    ip_address=models.CharField(max_length=100)
    machine_user=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.hostname + " ip : " + self.ip_address

    class Meta :
        db_table = "ordinateur"

class Run(models.Model) :
    id_run = models.AutoField(primary_key=True)
    nom_run = models.CharField(max_length=255)
    date_run = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)
    machine = models.ForeignKey(Sequenceur, related_name="runs", on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "run"

class Folder(models.Model) :
    id_folder = models.AutoField(primary_key=True)
    folderName = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    taille = models.BigIntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', null=True, related_name='children', on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'folder'

class Fichier(models.Model) :
    id_fichier = models.AutoField(primary_key=True)
    type=models.CharField(max_length=20)
    nom=models.CharField(max_length=255)
    date_creation=models.DateTimeField(auto_now_add=True)
    destinataire=models.IntegerField(null=True )
    run = models.ForeignKey(Run, related_name='run_fichiers', on_delete=models.CASCADE, blank=True, null=True)
    dossier = models.ForeignKey(Folder, related_name='fichiers', on_delete=models.CASCADE, blank=True, null=True)

    class Meta :
        db_table = "fichier"



class Analyse(models.Model) :
    id_analyse=models.AutoField(primary_key=True)
    date_analyse=models.DateField()
    name_analysis=models.CharField(max_length=255)

    class Meta:
        db_table = "analyse"

class Echantillon(models.Model) :
    id_echantillon = models.AutoField(primary_key=True) 
    libelle= models.CharField(max_length=255)
    date_echantillon = models.DateField()
    pays_origine = models.CharField(null=True, max_length=100)
    description = models.TextField()
    run = models.ForeignKey(Run, related_name='echantillons', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = "echantillon"


class DossierZip(models.Model):
    id_zip = models.AutoField(primary_key=True)
    nom_dossier = models.CharField(max_length=255)
    date_creation = models.DateField()

    class Meta:
        db_table = "dossierzip"

