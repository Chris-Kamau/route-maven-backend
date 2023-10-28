from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('number_plate', 'image', 'driver_name', 'driver_contact', 'route', 'gender')

# Register your models here.
admin.site.register(Todo, TodoAdmin)