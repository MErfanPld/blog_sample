from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from finance.models import Cost , Income , Debtor , Creditor

#*=========================== DELETE SERIALIZER ===========================*#

class DELETE_Cost_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Cost
        fields = ('id','is_active','date_deactivated')



class DELETE_Income_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Income
        fields = ('id','is_active','date_deactivated')



class DELETE_Debtor_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Debtor
        fields = ('id','is_active','date_deactivated')



class DELETE_Creditor_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Creditor
        fields = ('id','is_active','date_deactivated')


#*=========================== UPDATE / CREATE / LIST ===========================*#


class Cost_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Cost
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )



class Income_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Income
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )



class Debtor_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Debtor
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )



class Creditor_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Creditor
        exclude = (
            'date_deactivated',
            'date_edited',
            'id_base_record'
            )


