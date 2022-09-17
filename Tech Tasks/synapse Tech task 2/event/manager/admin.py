from django.contrib import admin
from .models import Event

# Register your models here.
@admin.register(Event)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','Event_Name','Start_Date','End_Date','No_of_People','Situation')
