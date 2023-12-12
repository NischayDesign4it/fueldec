from django.contrib import admin
from .models import (CustomUser, vehicle)

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(vehicle)