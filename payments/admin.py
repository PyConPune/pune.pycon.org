from django.contrib import admin

from payments.models import Invoice, Payment, Order, RazorpayKeys


@admin.register(Invoice)
class Invoice(admin.ModelAdmin):
    pass


@admin.register(Payment)
class Payment(admin.ModelAdmin):
    pass


@admin.register(Order)
class Order(admin.ModelAdmin):
    pass


@admin.register(RazorpayKeys)
class RazorpayKeys(admin.ModelAdmin):
    pass
