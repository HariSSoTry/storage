from django.db import models
from django.contrib.auth.models import User


# class Document(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class Folder(models.Model):
#     name = models.CharField(max_length=200)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     documents = models.ManyToManyField(Document)
#
#
# class Patient(models.Model):
#     name = models.CharField(max_length=200)
#     birthdate = models.DateField()
#     diagnosis = models.TextField()
#     symptoms = models.TextField()
#     allergies = models.TextField()
#     medical_history = models.TextField()
#     current_medication = models.TextField()
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
#
# class PatientDatabase(models.Model):
#     patients = models.ManyToManyField(Patient)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Symptom(models.Model):
    name = models.CharField(max_length=200)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Recommendation(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # author = models.CharField(max_length=200)
    # date = models.DateField()
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Disease(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    symptoms = models.ManyToManyField(Symptom)
    treatment_recommendations = models.TextField()
    # additional_documents = models.ManyToManyField(Document)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

