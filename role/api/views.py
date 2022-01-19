from rest_framework.generics import CreateAPIView
from .serializers import RoleSerializer
from ..models import RolesModel
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from usermanager.models import User


class CreateNameView(CreateAPIView):
    queryset = RolesModel.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminUser]


class CreateRoleView(CreateAPIView):
    new_group, created = Group.objects.get_or_create(name='new_group')
    ct = ContentType.objects.get_for_model(User)
    # permission = Permission.objects.create(codename='can_go_haridwar', name='Can go to Haridwar', content_type=ct)
    # new_group.permissions.add(permission)
