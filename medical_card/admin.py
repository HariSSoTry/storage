from django.contrib import admin
from .models import *

admin.site.register(Symptom)
# admin.site.register(Diagnosis)
admin.site.register(Document)


class RecommendationInline(admin.TabularInline):
    model = Recommendation
    extra = 1


# admin.site.register(Disease)
@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    # list_display = ("title", "related_fields")
    inlines = [RecommendationInline]
    # def related_fields(self, obj):
    #     related_model = RelatedModel.objects.get(pk=obj.related_model_id)
    #     return related_model.field1, related_model.field2
    # related_fields.short_description = 'Related Fields'


class DiseaseInLine(admin.TabularInline):
    model = Disease
    extra = 1
    show_change_link = True  # Ссылка на страницу редактирования болезни


# admin.site.register(Recommendation)
@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "disease",
        # "related_fields",
        # "content",
    )

    list_filter = "disease", "title"
    readonly_fields = ('get_related_field1', 'get_related_field2',)
    search_fields = "disease__name", "title"

    def get_related_field1(self, obj):
        return obj.disease.name

    get_related_field1.short_description = 'Заболевание'

    def get_related_field2(self, obj):
        return obj.disease.description

    get_related_field2.short_description = 'Описание заболевания'

    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['related_fields'] = Disease.objects.filter(pk=object_id)
    #     return super().change_view(
    #         request, object_id, form_url, extra_context=extra_context,
    #     )

    # def related_fields(self, obj):
    #     disease = Disease.objects.get(pk=obj.disease_id)
    #     return disease.name
    #
    # related_fields.short_description = 'Заболевание'


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    # inlines = [DiseaseInLine]
    readonly_fields = ('get_related_field3',)

    def get_related_field3(self, obj):
        return obj.disease.description

    get_related_field3.short_description = 'Описание заболевания'
# class DiagnosisInline(admin.TabularInline):
#     model = Diagnosis
#     extra = 0
#     show_change_link = True


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "birthdate")
    search_fields = ("last_name", "first_name")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    readonly_fields = ('get_recommendations',)

    def get_recommendations(self, obj):
        diagnosis = obj.diagnosis
        disease = diagnosis.disease
        recommendations = Recommendation.objects.filter(disease=disease)
        return ', '.join([rec.title for rec in recommendations])

    get_recommendations.short_description = 'Рекомендации'

    # get_related_field1.short_description = 'Диагноз'
    # get_related_field2.short_description = 'Рекомендации'
    # list_display = ('id', 'get_recommendations')

    # def get_related_field1(self, obj):
    #     return obj.disease.recommendation_set.name

    # @staticmethod
    # def get_related_field2(self, obj):
    #     return obj.disease.recommendation_set

    # inlines = [RelatedModel1Inline, RelatedModel2Inline]