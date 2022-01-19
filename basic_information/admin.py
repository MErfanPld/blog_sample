from django.contrib import admin
from .models import OwnerInformation, FarmInformation, HallInformation, StandardInformation, DurationInformation, ChickenInformation, BlackoutProgram, DietPlan, VaccineProgramInformation

# Register your models here.


class OwnerInformationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'first_name',
                    'number_of_farms', 'total_capacity',)
    list_filter = ('number_of_farms',)
    search_fields = ('first_name', 'first_name', 'number_of_farms',
                     'total_capacity',)
    ordering = ['number_of_farms']


admin.site.register(OwnerInformation, OwnerInformationAdmin)


class FarmInformationAdmin(admin.ModelAdmin):
    list_display = ('farm_name', 'number_of_halls',
                    'farm_capacity',)
    list_filter = ('number_of_halls', 'farm_capacity',)
    search_fields = ('farm_name', 'number_of_halls',
                     'farm_capacity',)
    ordering = ['number_of_halls']


admin.site.register(FarmInformation, FarmInformationAdmin)


class HallInformationAdmin(admin.ModelAdmin):
    list_display = ('hall_number', 'capacity',)
    list_filter = ('hall_number', 'capacity',)
    search_fields = ('hall_number', 'capacity',)
    ordering = ['hall_number']


admin.site.register(HallInformation, HallInformationAdmin)


#class StandardInformationAdmin(admin.ModelAdmin):
#    list_display = ("number_of_casualties", "elimination_number", "toـcutـoffـtheـhead", "total_losses", "cumulative_losses",
#                    "consumed_seeds", "collective_seeds", "per_capita_consumption", "weight", "daily_weight_gain", "average_room_temperature",)
#    search_fields = ("number_of_casualties", "elimination_number", "toـcutـoffـtheـhead", "total_losses", "cumulative_losses",
#                     "consumed_seeds", "collective_seeds", "per_capita_consumption", "weight", "daily_weight_gain", "average_room_temperature",)


#admin.site.register(StandardInformation, StandardInformationAdmin)

admin.site.register(StandardInformation)
admin.site.register(DurationInformation)
admin.site.register(ChickenInformation)
admin.site.register(BlackoutProgram)
admin.site.register(DietPlan)
admin.site.register(VaccineProgramInformation)
