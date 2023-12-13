from django.contrib import admin
from .models import (CustomUser, vehicle, transactions)

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(vehicle)
admin.site.register(transactions)

