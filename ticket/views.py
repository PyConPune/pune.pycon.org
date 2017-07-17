from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from ticket.models import Ticket, UserTicket
from ticket.forms import TicketApplicationForm


class TicketApplicationView(TemplateView):

    form_class = TicketApplicationForm
    template_name = 'ticket/application.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        tickets = Ticket.objects.all()
        return render(request, self.template_name, {'form': form, 'tickets': tickets})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/account/signup/')
        if form.is_valid():
            ticket = form.cleaned_data['ticket']
            userticketcount = UserTicket.objects.filter(ticket=ticket).count()
            if userticketcount < ticket.limit:
                userticket = UserTicket(user=request.user, ticket=ticket)
                userticket.save()
                return HttpResponseRedirect('/ticket/thanks/')
        return render(request, self.template_name, {'form': form, 'tickets': tickets})


def thanks(request):
    return render(request, 'ticket/thanks.html')
