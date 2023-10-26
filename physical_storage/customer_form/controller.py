from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from accounts.models import User
from accounts.serializers import UserSerializer
from .models import PhyscialStorageForm
from .serializers import PhyscialStorageFormSerializer

class FormController:
    @staticmethod
    def get_user_with_forms_by_id(pk=None):
        user = get_object_or_404(User, id=pk)
        user_serializer = UserSerializer(user)
        data = user_serializer.data

        customer_forms = PhyscialStorageForm.objects.filter(userid=user)

        if customer_forms.exists():
            customer_forms_serializer = PhyscialStorageFormSerializer(customer_forms, many=True)
            data['customer_forms'] = customer_forms_serializer.data
        else:
            data['customer_forms'] = "This user currently has no forms."

        return JsonResponse(data)
