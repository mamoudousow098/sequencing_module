from django.contrib import admin
from sequencing_module_api.models import *

# Register your models here.
admin.register(User)
admin.register(Echantillon)
admin.register(DossierZip)
admin.register(Fichier)
admin.register(Ordinateur)
admin.register(Run)

