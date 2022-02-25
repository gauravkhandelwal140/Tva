from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *
router=DefaultRouter()
router.register('users',User_viewset,basename='survey')
urlpatterns = [
     path('api/',include(router.urls)),

]
