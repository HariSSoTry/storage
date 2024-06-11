from django.contrib import admin
from .models import *

admin.site.register(Symptom)
admin.site.register(Disease)
admin.site.register(Recommendation)
admin.site.register(Patient)
admin.site.register(Diagnosis)
admin.site.register(Document)
admin.site.register(Appointment)
