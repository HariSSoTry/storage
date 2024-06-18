from django.contrib import admin
from .models import *

admin.site.register(Symptom)
admin.site.register(Disease)


# admin.site.register(Recommendation)
@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ("title", "disease")
    list_filter = "disease", "title"


# admin.site.register(Patient)
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "birthdate")


admin.site.register(Diagnosis)
admin.site.register(Document)
admin.site.register(Appointment)
