from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(HeadDoctor)
admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)