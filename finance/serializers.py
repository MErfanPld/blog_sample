#   https://javafarsi.com/2020/12/%D8%B3%D8%A7%D8%AE%D8%AA-api-%D8%AF%D8%B1-%D8%AC%D9%86%DA%AF%D9%88-%D8%A8%D8%A7-%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-django-rest-framework/#%D9%86%D8%B5%D8%A8_Django_Rest_Framework_%D8%AF%D8%B1_venv_%D9%BE%D8%B1%D9%88%DA%98%D9%87

from rest_framework import serializers
from .models import Cost


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = ['id', 'cost_title', 'cost_date', 'cost_amount', 'cost_description']
