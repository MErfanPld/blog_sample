from breeding_management.api.serializers import DELETE_Weightlifting_Serializer
from django.db.models import query_utils
from django.db.models.query import QuerySet
from rest_framework import generics
from .serializers import Cost_Serializer, Creditor_Serializer, DELETE_Cost_Serializer, Debtor_Serializer, Income_Serializer
from finance.models import Creditor, Cost, Debtor, Income
from django.utils import timezone
from rest_framework.response import Response
from .serializers import DELETE_Cost_Serializer , DELETE_Creditor_Serializer , DELETE_Debtor_Serializer , DELETE_Income_Serializer

#*=========================== DELETEAPIView ===========================*#

# we dont acctualy delete anything
# just mark them as deleted
# --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

class Cost_APIView_Delete (generics.UpdateAPIView):
    queryset = Cost.objects.all()
    serializer_class = DELETE_Cost_Serializer


class Debtor_APIVeiw_Delete (generics.UpdateAPIView):
    queryset = Debtor.objects.all()
    serializer_class = DELETE_Debtor_Serializer


class Income_APIVeiw_Delete (generics.UpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = DELETE_Income_Serializer


class Creditor_APIVeiw_Delete (generics.UpdateAPIView):
    queryset = Creditor.objects.all()
    serializer_class = DELETE_Creditor_Serializer



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


class Cost_APIView_Update (generics.UpdateAPIView):
    queryset = Cost.objects.all()
    serializer_class = Cost_Serializer
    model = Cost
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

class Debtor_APIVeiw_Update (generics.UpdateAPIView):
    queryset = Debtor.objects.all()
    serializer_class = Debtor_Serializer
    model = Debtor
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

class Income_APIVeiw_Update (generics.UpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = Income_Serializer
    model = Income
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

class Creditor_APIVeiw_Update (generics.UpdateAPIView):
    queryset = Creditor.objects.all()
    serializer_class = Creditor_Serializer
    model = Creditor
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
#*=========================== ListAPIView ===========================*#


class Cost_APIView_List (generics.ListAPIView):
    queryset = Cost.objects.all()
    serializer_class = Cost_Serializer


class Debtor_APIVeiw_List (generics.ListAPIView):
    queryset = Debtor.objects.all()
    serializer_class = Debtor_Serializer


class Income_APIVeiw_List (generics.ListAPIView):
    queryset = Income.objects.all()
    serializer_class = Income_Serializer


class Creditor_APIVeiw_List (generics.ListAPIView):
    queryset = Creditor.objects.all()
    serializer_class = Creditor_Serializer

#*=========================== ListCreateAPIView ===========================*#


class Cost_APIView (generics.ListCreateAPIView):
    queryset = Cost.objects.all()
    serializer_class = Cost_Serializer


class Debtor_APIVeiw (generics.ListCreateAPIView):
    queryset = Debtor.objects.all()
    serializer_class = Debtor_Serializer


class Income_APIVeiw (generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = Income_Serializer


class Creditor_APIVeiw (generics.ListCreateAPIView):
    queryset = Creditor.objects.all()
    serializer_class = Creditor_Serializer
