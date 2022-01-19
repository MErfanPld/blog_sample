from django.db import models
from django.db.models import query_utils
from django.db.models.base import Model
from django.db.models.query import QuerySet
from rest_framework import generics
from rest_framework.response import Response
from django.utils import timezone
from .serializers import OwnerInformation_Serializer, BlackoutProgram_Serializer, ChickenInformation_Serializer, FarmInformation_Serializer, StandardInformation_Serializer
from .serializers import DietPlan_Serializer, HallInformation_Serializer, DurationInformation_Serializer, VaccineProgramInformation_Serializer, StoreRoom_Serializer , Vaccin_Serializer
from basic_information.models import (
    OwnerInformation, BlackoutProgram, ChickenInformation, FarmInformation,
    StandardInformation, VaccineProgramInformation, DurationInformation,
    HallInformation, DietPlan, StoreRoom , Vaccin )

from .serializers import DELETE_BlackoutProgram_Serializer , DELETE_ChickenInformation_Serializer , DELETE_DietPlan_Serializer , DELETE_DurationInformation_Serializer , DELETE_FarmInformation_Serializer
from .serializers import DELETE_VaccineProgramInformation_Serializer , DELETE_StoreRoom_Serializer , DELETE_OwnerInformation_Serializer , DELETE_Vaccin_Serializer , DELETE_StandardInformation_Serializer , DELETE_HallInformation_Serializer
from rest_framework.permissions import IsAuthenticated , AllowAny

#*=========================== DELETEAPIView ===========================*#

# we dont acctualy delete anything
# just mark them as deleted
# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *


class  OwnerInformation_APIView_Delete(generics.UpdateAPIView):
    queryset = OwnerInformation.objects.all()
    serializer_class = DELETE_OwnerInformation_Serializer

# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *
class Vaccin_APIView_Delete(generics.UpdateAPIView):
    queryset = Vaccin.objects.all()
    serializer_class = DELETE_Vaccin_Serializer

# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class BlackoutProgram_APIView_Delete (generics.UpdateAPIView):
    queryset = BlackoutProgram.objects.all()
    serializer_class = DELETE_BlackoutProgram_Serializer

# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class ChickenInformation_APIView_Delete (generics.UpdateAPIView):
    queryset = ChickenInformation.objects.all()
    serializer_class = DELETE_ChickenInformation_Serializer

# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class FarmInformation_APIView_Delete (generics.UpdateAPIView):
    queryset = FarmInformation.objects.all()
    serializer_class = DELETE_FarmInformation_Serializer

# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class StandardInformation_APIView_Delete (generics.UpdateAPIView):
    queryset = StandardInformation.objects.all()
    serializer_class = DELETE_StandardInformation_Serializer

# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class VaccineProgramInformation_APIView_Delete (generics.UpdateAPIView):
    queryset = VaccineProgramInformation.objects.all()
    serializer_class = DELETE_VaccineProgramInformation_Serializer

# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class DurationInformation_APIView_Delete (generics.UpdateAPIView):
    queryset = DurationInformation.objects.all()
    serializer_class = DELETE_DurationInformation_Serializer

# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class HallInformation_APIView_Delete (generics.UpdateAPIView):
    queryset = HallInformation.objects.all()
    serializer_class = DELETE_HallInformation_Serializer

# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class DietPlan_APIView_Delete (generics.UpdateAPIView):
    queryset = DietPlan.objects.all()
    serializer_class = DELETE_DietPlan_Serializer

# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class StoreRoom_APIView_Delete (generics.UpdateAPIView):
    queryset = StoreRoom.objects.all()
    serializer_class = DELETE_StoreRoom_Serializer


#*=========================== UpdateEditAPIView ===========================*#
def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # start overriding method
        self.create(id=instance.id)
        data = request.data
        # finish overriding method
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

def perform_update(self, serializer):
        serializer.save()

def create(self,id):
        obj = self.model.objects.get(pk=id)
        obj.pk = None # اگر این خط رو برداری ابجکت ساخته نمیشه
        obj.is_active=False
        obj.date_edited = timezone.now()
        obj.id_base_record = id
        obj.save()

# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class  OwnerInformation_APIView_Update(generics.UpdateAPIView):
    queryset = OwnerInformation.objects.all()
    serializer_class = OwnerInformation_Serializer
    model = OwnerInformation

    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        Response=update(self, request, *args, **kwargs)
        return Response

    def perform_update(self, serializer):
        perform_update(self, serializer)

    def partial_update(self, request, *args, **kwargs):
        partial_update(self, request, *args, **kwargs)

    def create(self,id):
        create(self,id)

# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *
class Vaccin_APIView_Update(generics.UpdateAPIView):
    queryset = Vaccin.objects.all()
    serializer_class = Vaccin_Serializer
    model = Vaccin
    
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        Response=update(self, request, *args, **kwargs)
        return Response

    def perform_update(self, serializer):
        perform_update(self, serializer)

    def partial_update(self, request, *args, **kwargs):
        partial_update(self, request, *args, **kwargs)

    def create(self,id):
        create(self,id)
# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class BlackoutProgram_APIView_Update (generics.UpdateAPIView):
    queryset = BlackoutProgram.objects.all()
    serializer_class = BlackoutProgram_Serializer
    model = BlackoutProgram
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        Response=update(self, request, *args, **kwargs)
        return Response

    def perform_update(self, serializer):
        perform_update(self, serializer)

    def partial_update(self, request, *args, **kwargs):
        partial_update(self, request, *args, **kwargs)

    def create(self,id):
        create(self,id)
# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class ChickenInformation_APIView_Update (generics.UpdateAPIView):
    queryset = ChickenInformation.objects.all()
    serializer_class = ChickenInformation_Serializer
    model = ChickenInformation
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        Response=update(self, request, *args, **kwargs)
        return Response

    def perform_update(self, serializer):
        perform_update(self, serializer)

    def partial_update(self, request, *args, **kwargs):
        partial_update(self, request, *args, **kwargs)

    def create(self,id):
        create(self,id)
# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class FarmInformation_APIView_Update (generics.UpdateAPIView):
    queryset = FarmInformation.objects.all()
    serializer_class = FarmInformation_Serializer
    model = FarmInformation
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        Response=update(self, request, *args, **kwargs)
        return Response

    def perform_update(self, serializer):
        perform_update(self, serializer)

    def partial_update(self, request, *args, **kwargs):
        partial_update(self, request, *args, **kwargs)

    def create(self,id):
        create(self,id)
# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class StandardInformation_APIView_Update (generics.UpdateAPIView):
    queryset = StandardInformation.objects.all()
    serializer_class = StandardInformation_Serializer
    model = StandardInformation
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        Response=update(self, request, *args, **kwargs)
        return Response

    def perform_update(self, serializer):
        perform_update(self, serializer)

    def partial_update(self, request, *args, **kwargs):
        partial_update(self, request, *args, **kwargs)

    def create(self,id):
        create(self,id)
# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class VaccineProgramInformation_APIView_Update (generics.UpdateAPIView):
    queryset = VaccineProgramInformation.objects.all()
    serializer_class = VaccineProgramInformation_Serializer
    model = VaccineProgramInformation
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        Response=update(self, request, *args, **kwargs)
        return Response

    def perform_update(self, serializer):
        perform_update(self, serializer)

    def partial_update(self, request, *args, **kwargs):
        partial_update(self, request, *args, **kwargs)

    def create(self,id):
        create(self,id)
# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class DurationInformation_APIView_Update (generics.UpdateAPIView):
    queryset = DurationInformation.objects.all()
    serializer_class = DurationInformation_Serializer
    model = DurationInformation
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        Response=update(self, request, *args, **kwargs)
        return Response


    def perform_update(self, serializer):
        perform_update(self, serializer)

    def partial_update(self, request, *args, **kwargs):
        partial_update(self, request, *args, **kwargs)

    def create(self,id):
        create(self,id)
# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class HallInformation_APIView_Update (generics.UpdateAPIView):
    queryset = HallInformation.objects.all()
    serializer_class = HallInformation_Serializer
    model = HallInformation
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        Response=update(self, request, *args, **kwargs)
        return Response

    def perform_update(self, serializer):
        perform_update(self, serializer)

    def partial_update(self, request, *args, **kwargs):
        partial_update(self, request, *args, **kwargs)

    def create(self,id):
        create(self,id)
# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class DietPlan_APIView_Update (generics.UpdateAPIView):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlan_Serializer
    model = DietPlan
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        Response=update(self, request, *args, **kwargs)
        return Response

    def perform_update(self, serializer):
        perform_update(self, serializer)

    def partial_update(self, request, *args, **kwargs):
        partial_update(self, request, *args, **kwargs)

    def create(self,id):
        create(self,id)
# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class StoreRoom_APIView_Update (generics.UpdateAPIView):
    queryset = StoreRoom.objects.all()
    serializer_class = StoreRoom_Serializer
    model = StoreRoom
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        Response=update(self, request, *args, **kwargs)
        return Response

    def perform_update(self, serializer):
        perform_update(self, serializer)

    def partial_update(self, request, *args, **kwargs):
        partial_update(self, request, *args, **kwargs)

    def create(self,id):
        create(self,id)

#*=========================== ListAPIView =============================*#

class Vaccin_APIView_List (generics.ListAPIView):
    queryset = Vaccin.objects.all()
    serializer_class = Vaccin_Serializer


    """
    List a queryset.
    """
    #def list(self, request, *args, **kwargs):
    #    queryset = self.filter_queryset(self.get_queryset())
#
    #    page = self.paginate_queryset(queryset)
    #    if page is not None:
    #        serializer = self.get_serializer(page, many=True)
    #        return self.get_paginated_response(serializer.data)
#
    #    serializer = self.get_serializer(queryset, many=True)
    #    # start filtering by is_active 
    #    return Response(serializer.data)

class OwnerInformation_APIView_List (generics.ListAPIView):
    queryset = OwnerInformation.objects.all()
    serializer_class = OwnerInformation_Serializer
    permission_classes = (IsAuthenticated,)


        


class BlackoutProgram_APIView_List (generics.ListAPIView):
    queryset = BlackoutProgram.objects.all()
    serializer_class = BlackoutProgram_Serializer


class ChickenInformation_APIView_List (generics.ListAPIView):
    queryset = ChickenInformation.objects.all()
    serializer_class = ChickenInformation_Serializer


class FarmInformation_APIView_List (generics.ListAPIView):
    queryset = FarmInformation.objects.all()
    serializer_class = FarmInformation_Serializer


class StandardInformation_APIView_List (generics.ListAPIView):
    queryset = StandardInformation.objects.all()
    serializer_class = StandardInformation_Serializer


class VaccineProgramInformation_APIView_List (generics.ListAPIView):
    queryset = VaccineProgramInformation.objects.all()
    serializer_class = VaccineProgramInformation_Serializer


class DurationInformation_APIView_List (generics.ListAPIView):
    queryset = DurationInformation.objects.all()
    serializer_class = DurationInformation_Serializer


class HallInformation_APIView_List (generics.ListAPIView):
    queryset = HallInformation.objects.all()
    serializer_class = HallInformation_Serializer


class DietPlan_APIView_List (generics.ListAPIView):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlan_Serializer


class StoreRoom_APIView_List (generics.ListAPIView):
    queryset = StoreRoom.objects.all()
    serializer_class = StoreRoom_Serializer


#*=========================== ListCreateAPIView ===========================*#

class OwnerInformation_APIView (generics.ListCreateAPIView):
    queryset = OwnerInformation.objects.all()
    serializer_class = OwnerInformation_Serializer
    permission_classes = (IsAuthenticated,)


class BlackoutProgram_APIView (generics.ListCreateAPIView):
    queryset = BlackoutProgram.objects.all()
    serializer_class = BlackoutProgram_Serializer


class ChickenInformation_APIView (generics.ListCreateAPIView):
    queryset = ChickenInformation.objects.all()
    serializer_class = ChickenInformation_Serializer


class FarmInformation_APIView (generics.ListCreateAPIView):
    queryset = FarmInformation.objects.all()
    serializer_class = FarmInformation_Serializer


class StandardInformation_APIView (generics.ListCreateAPIView):
    queryset = StandardInformation.objects.all()
    serializer_class = StandardInformation_Serializer


class VaccineProgramInformation_APIView (generics.ListCreateAPIView):
    queryset = VaccineProgramInformation.objects.all()
    serializer_class = VaccineProgramInformation_Serializer


class DurationInformation_APIView (generics.ListCreateAPIView):
    queryset = DurationInformation.objects.all()
    serializer_class = DurationInformation_Serializer


class HallInformation_APIView (generics.ListCreateAPIView):
    queryset = HallInformation.objects.all()
    serializer_class = HallInformation_Serializer


class DietPlan_APIView (generics.ListCreateAPIView):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlan_Serializer


class StoreRoom_APIView (generics.ListCreateAPIView):
    queryset = StoreRoom.objects.all()
    serializer_class = StoreRoom_Serializer

class Vaccin_APIView (generics.ListCreateAPIView):
    queryset = Vaccin.objects.all()
    serializer_class = Vaccin_Serializer
