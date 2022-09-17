from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='request'),
    path("update/<int:id>",views.update_data,name="updatedata"),
    path("delete/<int:id>",views.delete_data,name="deletedata"),
]