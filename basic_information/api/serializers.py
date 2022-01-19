from django.db.models import fields
from rest_framework import serializers
from basic_information.models import OwnerInformation, FarmInformation, HallInformation, StandardInformation, StoreRoom , Vaccin
from basic_information.models import DurationInformation, ChickenInformation, BlackoutProgram, DietPlan, VaccineProgramInformation


#*=========================== DELETE SERIALIZER ===========================*#

class DELETE_OwnerInformation_Serializer (serializers.ModelSerializer):
    class Meta:
        model = OwnerInformation
        fields = ('id','is_active','date_deactivated')

class DELETE_FarmInformation_Serializer (serializers.ModelSerializer):
    class Meta:
        model = FarmInformation
        fields = ('id','is_active','date_deactivated')

class DELETE_HallInformation_Serializer (serializers.ModelSerializer):
    class Meta:
        model = HallInformation
        fields = ('id','is_active','date_deactivated')

class DELETE_StandardInformation_Serializer (serializers.ModelSerializer):
    class Meta:
        model = StandardInformation
        fields = ('id','is_active','date_deactivated')

class DELETE_DurationInformation_Serializer (serializers.ModelSerializer):
    class Meta:
        model = DurationInformation
        fields = ('id','is_active','date_deactivated')

    
class DELETE_ChickenInformation_Serializer (serializers.ModelSerializer):
    class Meta:
        model = ChickenInformation
        fields = ('id','is_active','date_deactivated')

class DELETE_BlackoutProgram_Serializer (serializers.ModelSerializer):
    class Meta:
        model = BlackoutProgram
        fields = ('id','is_active','date_deactivated')

class DELETE_DietPlan_Serializer (serializers.ModelSerializer):
    class Meta:
        model = DietPlan
        fields = ('id','is_active','date_deactivated')

class DELETE_VaccineProgramInformation_Serializer (serializers.ModelSerializer):
    name=serializers.StringRelatedField()

    class Meta:
        model = VaccineProgramInformation
        fields = ('id','is_active','date_deactivated')

class DELETE_StoreRoom_Serializer (serializers.ModelSerializer):
    class Meta:
        model = StoreRoom
        fields = ('id','is_active','date_deactivated')

class DELETE_Vaccin_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Vaccin
        fields = ('id','is_active','date_deactivated')


#*=========================== UPDATE / CREATE / LIST ===========================*#

class OwnerInformation_Serializer (serializers.ModelSerializer):
    class Meta:
        model = OwnerInformation
        
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )


class FarmInformation_Serializer (serializers.ModelSerializer):
    class Meta:
        model = FarmInformation
        
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )


class HallInformation_Serializer (serializers.ModelSerializer):
    class Meta:
        model = HallInformation
        
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )


class StandardInformation_Serializer (serializers.ModelSerializer):
    class Meta:
        model = StandardInformation
        
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )


class DurationInformation_Serializer (serializers.ModelSerializer):
    class Meta:
        model = DurationInformation
        fields = (
            'duration_number', 'duration_season',
            'start_date', 'chicken_number',
        )
    

class ChickenInformation_Serializer (serializers.ModelSerializer):
    class Meta:
        model = ChickenInformation
        
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )


class BlackoutProgram_Serializer (serializers.ModelSerializer):
    class Meta:
        model = BlackoutProgram
        
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )


class DietPlan_Serializer (serializers.ModelSerializer):
    class Meta:
        model = DietPlan
        
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )


class VaccineProgramInformation_Serializer (serializers.ModelSerializer):
    name=serializers.StringRelatedField()
   
    class Meta:
        model = VaccineProgramInformation
        
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )


class StoreRoom_Serializer (serializers.ModelSerializer):
    class Meta:
        model = StoreRoom
        
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )


class Vaccin_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Vaccin
        
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )
