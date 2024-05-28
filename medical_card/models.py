from django.db import models
from django.contrib.auth.models import User


class Symptom(models.Model):
    description = models.CharField(max_length=200)


class Disease(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    symptoms = models.ManyToManyField(Symptom)

    def last_recommendation(self):
        pass


class Patient(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField(blank=True, null=True)
    # allergies = models.TextField()

    def current_medication(self):   # todo добавить как метод для пациента
        pass

    def medical_history(self):
        pass


class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    # date = models.DateField()


class Recommendation(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    # author = models.CharField(max_length=200)
    # date = models.DateField()


class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)


class Appointment(models.Model):
    # date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptoms = models.ManyToManyField(Symptom)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
