from django.contrib import admin

from ticket.models import Ticket, UserTicket, AuxiliaryTicket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass


@admin.register(AuxiliaryTicket)
class AuxiliaryTicketAdmin(admin.ModelAdmin):
    pass


@admin.register(UserTicket)
class UserTicketAdmin(admin.ModelAdmin):
    pass
