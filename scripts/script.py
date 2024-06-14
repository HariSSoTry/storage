from medical_card.models import *


def script_template():
    """
try: del sys.modules['scripts.script'];
except: pass
from scripts.script import script_template; script_template()
    """

    """Заполнение имени и фамилии"""
    # patients = Patient.objects.all()
    # for patient in patients:
    #     patient.last_name, patient.first_name = patient.name.split(' ')
    #     patient.save()
    #     print(patient.first_name, patient.last_name)

    """Заполнение даты рождения"""
    # import random
    # from datetime import datetime, timedelta
    #
    # start_date = datetime(1950, 1, 1)
    # end_date = datetime(2020, 12, 31)
    #
    # delta = end_date - start_date
    #
    # patients = Patient.objects.all()
    # for patient in patients:
    #
    #     random_days = random.randrange(delta.days)
    #     random_date = start_date + timedelta(days=random_days + 1)
    #
    #     patient.birthdate = random_date
    #
    #     print(f'{patient} {random_date}')
    #     patient.save()

    """Вывести последнюю рекомендацию по лечению бронхита"""
    # diseases = Disease.objects.filter(name__icontains='бронх')
    # disease = diseases.first()
    #
    # # for recommendation in disease.recommendation_set.all().order_by('date'):
    # #     print(recommendation.date, recommendation.title)
    #
    # # last_recommendation = disease.recommendation_set.all().order_by('date').last()
    # # print(last_recommendation)
    #
    # print(disease.last_recommendation())

    pass
