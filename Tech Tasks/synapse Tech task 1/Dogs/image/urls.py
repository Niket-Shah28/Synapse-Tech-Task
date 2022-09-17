from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='request'),
    path('photo/',views.image,name='request')
]