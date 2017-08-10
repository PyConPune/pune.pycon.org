from django.contrib import admin

from payments.models import Invoice


@admin.register(Invoice)
class Invoice(admin.ModelAdmin):
    pass
