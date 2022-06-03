from django.contrib import admin

from core.models import CustomUser, DriversLicense, Notice, PlateNumber

admin.site.register(CustomUser)
admin.site.register(DriversLicense)
admin.site.register(PlateNumber)
admin.site.register(Notice)
