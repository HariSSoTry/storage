from django.db import models
from django.contrib.auth.models import User


class Symptom(models.Model):
    """Симптомы"""
    description = models.CharField(max_length=200, verbose_name='Описание')

    class Meta:
        verbose_name = 'Симптом'
        verbose_name_plural = 'Симптомы'

    def __str__(self):
        return self.description


class Disease(models.Model):
    """Заболевания"""
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    symptoms = models.ManyToManyField(Symptom, verbose_name='Симптомы, соответствующие заболеванию')

    class Meta:
        verbose_name = 'Заболевание'
        verbose_name_plural = 'Заболевания'

    def __str__(self):
        return self.name

    def last_recommendation(self):
        pass


class Patient(models.Model):
    """Пациенты"""
    name = models.CharField(max_length=200, verbose_name='Имя Фамилия')
    birthdate = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    # allergies = models.TextField()

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def __str__(self):
        return self.name

    def current_medication(self):   # todo добавить как метод для пациента
        pass

    def medical_history(self):
        pass


class Diagnosis(models.Model):
    """
    Диагнозы

    Ставится после или во время осмотра
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Пациент')
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, verbose_name='Заболевание')
    # date = models.DateField()

    class Meta:
        verbose_name = 'Диагноз'
        verbose_name_plural = 'Диагнозы'

    def __str__(self):
        return f'Пациент: {self.patient}'


class Recommendation(models.Model):
    """
    Рекомендации по лечению определенного диагноза

    Может быть актуальным по дате
    """
    title = models.CharField(max_length=200, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, verbose_name='Заболевание')
    # author = models.CharField(max_length=200)
    # date = models.DateField()

    class Meta:
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекомендации'

    def __str__(self):
        return self.title  # todo Добавить заболевание


class Document(models.Model):
    """Документы"""
    title = models.CharField(max_length=200, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Пациент')
    link = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.title


class Appointment(models.Model):
    """
    Событие приёма у врача

    Диагноз может проставляться как сразу, так и после осмотра
    """
    # date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Пациент')
    symptoms = models.ManyToManyField(Symptom, verbose_name='Симптомы, озвученные на осмотре')
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE, verbose_name='Диагноз')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Документы')

    class Meta:
        verbose_name = 'Приём'
        verbose_name_plural = 'Приёмы'

    def __str__(self):
        return f'Пациент: {self.patient}'
