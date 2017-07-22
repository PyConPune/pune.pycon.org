from django.conf.urls import url

import ticket.views

urlpatterns = [
    url(r"^(?P<year>\d{4})/register/$", ticket.views.TicketApplicationView.as_view(),
        name="ticket_register"),

    url(r"^(?P<year>\d{4})/acknowledge/^$", ticket.views.acknowledge,
        name="ticet_acknowledge"),
]
