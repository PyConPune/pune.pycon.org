from django.contrib import admin

from inventory.models import Tshirt, UserTshirt


@admin.register(Tshirt)
class TshirtAdmin(admin.ModelAdmin):
    pass


@admin.register(UserTshirt)
class UserTshirtAdmin(admin.ModelAdmin):
    pass
