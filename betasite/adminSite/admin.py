from django.contrib import admin

from adminSite import models

admin.site.register(models.Class)
admin.site.register(models.Donor)
admin.site.register(models.Events)
admin.site.register(models.Donation)
admin.site.register(models.Transaction)