from django.shortcuts import render
from django.views.generic import TemplateView

from ticket.forms import TicketDetailsForm, TicketApplicationForm


class TicketDetailsView(TemplateView):

    form_class = TicketDetailsForm
    template_name = 'ticket/detail.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class TicketApplicationView(TemplateView):

    form_class = TicketApplicationForm
    template_name = 'ticket/application.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
