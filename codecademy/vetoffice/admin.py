from django.contrib import admin

# Import Owner and Patient models below:
from .models import Owner, Patient

# Register your models below:
admin.site.register(Owner)
admin.site.register(Patient)
