from django.contrib import admin
from .models import DrugRegistration , VaccineRegistration , ExperimentRegistration
from .models import Daily_Informations



admin.site.register(DrugRegistration)
admin.site.register(VaccineRegistration)
admin.site.register(ExperimentRegistration)
admin.site.register(Daily_Informations)


# class WeightliftingAdmin(admin.ModelAdmin):
#     list_display = ()
#     list_filter = ()
#     search_fields = ()
#     ordering = ['']


# admin.site.register(Weightlifting)


# class GeneralConditionAdmin(admin.ModelAdmin):
#     list_display = ()
#     list_filter = ()
#     search_fields = ()
#     ordering = ['']


# admin.site.register(GeneralCondition)


# class CortexAdmin(admin.ModelAdmin):
#     list_display = ()
#     list_filter = ()
#     search_fields = ()
#     ordering = ['']


# admin.site.register(Cortex)
