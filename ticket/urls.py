from django.conf.urls import url

import ticket.views

urlpatterns = [
    url(r"^register/$", ticket.views.TicketApplicationView.as_view(),
        name="ticket_register"),

    url(r"^acknowledge/^$", ticket.views.acknowledge,
        name="ticket_acknowledge"),
]
