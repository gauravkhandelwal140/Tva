from rest_framework import serializers
from .models import *
from rest_framework import filters


class User_serializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','company_name','age','city','state','zip','web','email',]


