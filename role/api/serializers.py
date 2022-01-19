from rest_framework import serializers
from role.models import RolesModel


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesModel
        fields = "__all__"
