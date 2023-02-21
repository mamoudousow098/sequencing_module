from django.contrib import admin
from sequencing_module_api.models import *

# site.register your models here.
admin.site.register(User)
admin.site.register(Echantillon)
admin.site.register(DossierZip)
admin.site.register(Fichier)
admin.site.register(Ordinateur)
admin.site.register(Run)

