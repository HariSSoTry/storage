from django.urls import path
from . import views

urlpatterns = [
    path('add_patient/', views.add_patient, name='add_patient'),
    path('view_patient_info/<str:name>/', views.view_patient_info, name='view_patient_info'),
    path('list_all_patients/', views.list_all_patients, name='list_all_patients'),
    path('search_patients/<str:search_term>/', views.search_patients, name='search_patients'),
    path('add_document_for_patient/<str:patient_name>/<str:document_title>/<str:document_content>/', views.add_document_for_patient, name='add_document_for_patient'),
    path('add_recommendation/<str:title>/<str:content>/<str:author>/<str:date>/', views.add_recommendation, name='add_recommendation'),
    path('view_recommendations/', views.view_recommendations, name='view_recommendations'),
    path('search_recommendations/<str:search_term>/', views.search_recommendations, name='search_recommendations'),
    path('add_disease/<str:name>/<str:description>/<str:symptoms>/<str:treatment_recommendations>/', views.add_disease, name='add_disease'),
    path('view_disease_info/<str:name>/', views.view_disease_info, name='view_disease_info'),
    path('list_diseases/', views.list_diseases, name='list_diseases'),
    path('search_diseases/<str:search_term>/', views.search_diseases, name='search_diseases'),
    path('add_treatment_recommendation/<str:disease_name>/<str:recommendation>/', views.add_treatment_recommendation, name='add_treatment_recommendation'),
    path('add_additional_document/<str:disease_name>/<str:document>/', views.add_additional_document, name='add_additional_document'),
    path('delete_disease/<str:name>/', views.delete_disease, name='delete_disease'),
    path('add_symptom/<str:symptom_name>/', views.add_symptom, name='add_symptom'),
    path('add_symptom_to_disease/<str:disease_name>/<str:symptom_name>/', views.add_symptom_to_disease, name='add_symptom_to_disease'),
    path('list_symptoms/', views.list_symptoms, name='list_symptoms'),
    path('search_diseases_by_symptom/<str:symptom_name>/', views.search_diseases_by_symptom, name='search_diseases_by_symptom'),
]
