from rest_framework import viewsets
from .models import PhyscialStorageForm
from .serializers import PhyscialStorageFormSerializer
from rest_framework import viewsets, generics, response
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .controller import FormController
class PhysicalStorageFormViewSet(viewsets.ModelViewSet):
    queryset = PhyscialStorageForm.objects.all()
    serializer_class = PhyscialStorageFormSerializer

    @action(detail=True, methods=['GET'], name='Get Highlight')
    def with_user(self, request, pk=None):
      return FormController.get_user_with_forms_by_id(pk)



    