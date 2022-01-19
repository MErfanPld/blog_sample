from django.db.models import query_utils
from django.db.models.query import QuerySet
from rest_framework import generics
from .serializers import Daily_information_Serializer, Weightlifting_Serializer, ExperimentRegistration_Serializer
from .serializers import VaccineRegistration_Serializer, DrugRegistration_Serializer
from breeding_management.models import Daily_Informations, Weightlifting, ExperimentRegistration, VaccineRegistration, DrugRegistration
from django.utils import timezone
from rest_framework.response import Response
from .serializers import DELETE_Daily_information_Serializer , DELETE_DrugRegistration_Serializer , DELETE_ExperimentRegistration_Serializer , DELETE_VaccineRegistration_Serializer , DELETE_Weightlifting_Serializer

#*=========================== DELETEAPIView ===========================*#

# we dont acctualy delete anything
# just mark them as deleted

class Daily_information_APIView_Delete (generics.UpdateAPIView):
    queryset = Daily_Informations.objects.all()
    serializer_class = DELETE_Daily_information_Serializer

    

class Weightlifting_APIVeiw_Delete (generics.UpdateAPIView):
    queryset = Weightlifting.objects.all()
    serializer_class = DELETE_Weightlifting_Serializer


class ExperimentRegistration_APIVeiw_Delete (generics.UpdateAPIView):
    queryset = ExperimentRegistration.objects.all()
    serializer_class = DELETE_ExperimentRegistration_Serializer


class VaccineRegistration_APIVeiw_Delete (generics.UpdateAPIView):
    queryset = VaccineRegistration.objects.all()
    serializer_class = DELETE_VaccineRegistration_Serializer


class DrugRegistration_APIVeiw_Delete (generics.UpdateAPIView):
    queryset = DrugRegistration.objects.all()
    serializer_class = DELETE_DrugRegistration_Serializer


#*=========================== ListEditAPIView ===========================*#
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
class Daily_information_APIView_Update (generics.UpdateAPIView):
    queryset = Daily_Informations.objects.all()
    serializer_class = Daily_information_Serializer
    model = Daily_Informations
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

class Weightlifting_APIVeiw_Update (generics.UpdateAPIView):
    queryset = Weightlifting.objects.all()
    serializer_class = Weightlifting_Serializer
    model = Weightlifting
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

class ExperimentRegistration_APIVeiw_Update (generics.UpdateAPIView):
    queryset = ExperimentRegistration.objects.all()
    serializer_class = ExperimentRegistration_Serializer
    model = ExperimentRegistration
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

class VaccineRegistration_APIVeiw_Update (generics.UpdateAPIView):
    queryset = VaccineRegistration.objects.all()
    serializer_class = VaccineRegistration_Serializer
    model = VaccineRegistration
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

class DrugRegistration_APIVeiw_Update (generics.UpdateAPIView):
    queryset = DrugRegistration.objects.all()
    serializer_class = DrugRegistration_Serializer
    model = DrugRegistration
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


#*=========================== ListAPIView ===========================*#


class Daily_information_APIView_List (generics.ListAPIView):
    queryset = Daily_Informations.objects.all()
    serializer_class = Daily_information_Serializer


class Weightlifting_APIVeiw_List (generics.ListAPIView):
    queryset = Weightlifting.objects.all()
    serializer_class = Weightlifting_Serializer


class ExperimentRegistration_APIVeiw_List (generics.ListAPIView):
    queryset = ExperimentRegistration.objects.all()
    serializer_class = ExperimentRegistration_Serializer


class VaccineRegistration_APIVeiw_List (generics.ListAPIView):
    queryset = VaccineRegistration.objects.all()
    serializer_class = VaccineRegistration_Serializer


class DrugRegistration_APIVeiw_List (generics.ListAPIView):
    queryset = DrugRegistration.objects.all()
    serializer_class = DrugRegistration_Serializer


#*=========================== ListCreateAPIView ===========================*#

class Daily_information_APIView (generics.ListCreateAPIView):
    queryset = Daily_Informations.objects.all()
    serializer_class = Daily_information_Serializer


class Weightlifting_APIVeiw (generics.ListCreateAPIView):
    queryset = Weightlifting.objects.all()
    serializer_class = Weightlifting_Serializer


class ExperimentRegistration_APIVeiw (generics.ListCreateAPIView):
    queryset = ExperimentRegistration.objects.all()
    serializer_class = ExperimentRegistration_Serializer


class VaccineRegistration_APIVeiw (generics.ListCreateAPIView):
    queryset = VaccineRegistration.objects.all()
    serializer_class = VaccineRegistration_Serializer


class DrugRegistration_APIVeiw (generics.ListCreateAPIView):
    queryset = DrugRegistration.objects.all()
    serializer_class = DrugRegistration_Serializer
