from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def add_patient(request, name, birthdate, diagnosis, symptoms, allergies, medical_history, current_medication):
    Patient.objects.create(
        name=name,
        birthdate=birthdate,
        diagnosis=diagnosis,
        symptoms=symptoms,
        allergies=allergies,
        medical_history=medical_history,
        current_medication=current_medication,
        owner=request.user
    )
    return render(request, 'success.html')


@login_required
def view_patient_info(request, name):
    patient = Patient.objects.filter(name__icontains=name, owner=request.user).first()
    if patient:
        context = {
            'patient': patient,
        }
        return render(request, 'patient_info.html', context)
    else:
        return render(request, 'error.html')


@login_required
def list_all_patients(request):
    patients = Patient.objects.filter(owner=request.user)
    context = {
        'patients': patients,
    }
    return render(request, 'patients_list.html', context)


@login_required
def search_patients(request, search_term):
    patients = Patient.objects.filter(name__icontains=search_term, owner=request.user)
    context = {
        'patients': patients,
    }
    return render(request, 'patients_list.html', context)


@login_required
def add_document_for_patient(request, patient_name, document_title, document_content):
    patient = Patient.objects.filter(name__icontains=patient_name, owner=request.user).first()
    if patient:
        document = Document.objects.create(
            title=document_title,
            content=document_content,
            owner=request.user
        )
        patient.documents.add(document)
        return render(request, 'success.html')
    else:
        return render(request, 'error.html')


@login_required
def add_recommendation(request, title, content, author, date):
    Recommendation.objects.create(
        title=title,
        content=content,
        author=author,
        date=date,
        owner=request.user
    )
    return render(request, 'success.html')


@login_required
def view_recommendations(request):
    recommendations = Recommendation.objects.filter(owner=request.user)
    context = {
        'recommendations': recommendations,
    }
    return render(request, 'recommendations_list.html', context)


@login_required
def search_recommendations(request, search_term):
    recommendations = Recommendation.objects.filter(title__icontains=search_term, owner=request.user)
    context = {
        'recommendations': recommendations,
    }
    return render(request, 'recommendations_list.html', context)


@login_required
def add_disease(request, name, description, symptoms, treatment_recommendations):
    disease = Disease.objects.create(
        name=name,
        description=description,
        owner=request.user
    )
    for symptom_name in symptoms.split(','):
        symptom, _ = Symptom.objects.get_or_create(name=symptom_name, owner=request.user)
        disease.symptoms.add(symptom)
    disease.treatment_recommendations = treatment_recommendations
    disease.save()
    return render(request, 'success.html')


@login_required
def view_disease_info(request, name):
    disease = Disease.objects.filter(name__icontains=name, owner=request.user).first()
    if disease:
        context = {
            'disease': disease,
        }
        return render(request, 'disease_info.html', context)
    else:
        return render(request, 'error.html')


@login_required
def list_diseases(request):
    diseases = Disease.objects.filter(owner=request.user)
    context = {
        'diseases': diseases,
    }
    return render(request, 'diseases_list.html', context)


@login_required
def search_diseases(request, search_term):
    diseases = Disease.objects.filter(name__icontains=search_term, owner=request.user)
    context = {
        'diseases': diseases,
    }
    return render(request, 'diseases_list.html', context)


@login_required
def add_treatment_recommendation(request, disease_name, recommendation):
    disease = Disease.objects.filter(name__icontains=disease_name, owner=request.user).first()
    if disease:
        disease.treatment_recommendations += recommendation
        disease.save()
        return render(request, 'success.html')
    else:
        return render(request, 'error.html')


@login_required
def add_additional_document(request, disease_name, document):
    disease = Disease.objects.filter(name__icontains=disease_name, owner=request.user).first()
    if disease:
        document = Document.objects.create(
            title=document,
            owner=request.user
        )
        disease.additional_documents.add(document)
        return render(request, 'success.html')
    else:
        return render(request, 'error.html')


@login_required
def delete_disease(request, name):
    disease = Disease.objects.filter(name__icontains=name, owner=request.user).first()
    if disease:
        disease.delete()
        return render(request, 'success.html')
    else:
        return render(request, 'error.html')


@login_required
def add_symptom(request, symptom_name):
    symptom, _ = Symptom.objects.get_or_create(name=symptom_name, owner=request.user)
    return render(request, 'success.html')


@login_required
def add_symptom_to_disease(request, disease_name, symptom_name):
    disease = Disease.objects.filter(name__icontains=disease_name, owner=request.user).first()
    if disease:
        symptom, _ = Symptom.objects.get_or_create(name=symptom_name, owner=request.user)
        disease.symptoms.add(symptom)
        return render(request, 'success.html')
    else:
        return render(request, 'error.html')


@login_required
def list_symptoms(request):
    symptoms = Symptom.objects.filter(owner=request.user)
    context = {
        'symptoms': symptoms,
    }
    return render(request, 'symptoms_list.html', context)


@login_required
def search_diseases_by_symptom(request, symptom_name):
    disease_names = Disease.objects.filter(symptoms__name__icontains=symptom_name, owner=request.user).values_list('name', flat=True)
    context = {
        'disease_names': disease_names,
    }
    return render(request, 'diseases_list.html', context)
