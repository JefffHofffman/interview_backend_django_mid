from django.shortcuts import render

# https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins
from datetime import datetime
from rest_framework import mixins
from rest_framework import generics

#TODO relative pkg ref
from interview.inventory.models import Inventory
from interview.inventory.serializers import InventorySerializer


class InventoryList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Inventory.objects.all()
        filt={}
        #TODO may need to convert/validate param into datetime
        min_created = self.request.query_params.get('min_created')
        if min_created is not None:
            filt.update(created_at__gte=min_created)
        #TODO other params
        queryset = queryset.filter(**filt)
        return queryset


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# Create your views here.
