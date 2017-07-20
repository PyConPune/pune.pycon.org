from django.conf.urls import url

import ticket.views

urlpatterns = [
    url(r"^ticket/buy/$", ticket.views.TicketApplicationView.as_view(), name="ticket_application"),
    url(r"^ticket/thanks/$", ticket.views.thanks, name="thanks"),
    url(r"^ticket/register/$", ticket.views.registration, name="registration"),
]
