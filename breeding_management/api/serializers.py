from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from breeding_management.models import Daily_Informations , Weightlifting , ExperimentRegistration
from breeding_management.models import VaccineRegistration , DrugRegistration


#*=========================== DELETE SERIALIZER ===========================*#

class DELETE_Daily_information_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Daily_Informations
        fields = ('id','is_active','date_deactivated')
  

class DELETE_Weightlifting_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Weightlifting
        fields = ('id','is_active','date_deactivated')


class DELETE_ExperimentRegistration_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = ExperimentRegistration
        fields = ('id','is_active','date_deactivated')

class DELETE_VaccineRegistration_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = VaccineRegistration    
        fields = ('id','is_active','date_deactivated')


class DELETE_DrugRegistration_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = DrugRegistration
        fields = ('id','is_active','date_deactivated')



#*=========================== UPDATE / CREATE / LIST ===========================*#

class Daily_information_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Daily_Informations
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        daily = Daily_Informations()
        total_loses = daily.Total_Losses()
        total_seed = daily.Total_Seed()
        try :
            ret['total_losses'] = total_loses
        except:
            print('error')
        try:
            ret['total_seed'] = total_seed
        except :
            print('error')
        return ret


class Weightlifting_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Weightlifting
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )


class ExperimentRegistration_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = ExperimentRegistration
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )

class VaccineRegistration_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = VaccineRegistration    
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )


class DrugRegistration_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = DrugRegistration
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )

