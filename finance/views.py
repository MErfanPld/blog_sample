from django.shortcuts import render
from .models import Cost
from rest_framework import generics
from .serializers import CostSerializer
 
 
class PostList(generics.ListCreateAPIView):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer