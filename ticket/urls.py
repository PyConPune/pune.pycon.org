from django.conf.urls import url

import ticket.views

urlpatterns = [
    url(r"^ticket/detail/$", ticket.views.TicketDetailsView.as_view(), name="ticket_detail"),
    url(r"^ticket/buy/$", ticket.views.TicketApplicationView.as_view(), name="ticket_application"),
]
