from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required

from payments.models import Invoice, RazorpayKeys
from ticket.models import Ticket, UserTicket, AuxiliaryTicket
from payments.razorpay.razorpay_payments import RazorpayPayments
from payments.models import Payment, Order

import json

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        keys = RazorpayKeys.objects.first()
        payment = RazorpayPayments(keys.api_key, keys.api_secret)
        data = json.loads(request.body)
        if 'payload' not in data or 'invoice' not in data['payload']:
            return JsonResponse({"message": "Invalid Data"})

        invoice_entity = data['payload']['invoice']['entity']
        order_entity = data['payload']['order']['entity']
        payment_entity = data['payload']['payment']['entity']

        invoice = Invoice.objects.get(invoice_id=invoice_entity['id'])
        invoice.status = invoice_entity['status']
        invoice.save()
        payment.save_payment(payment_entity)
        payment.save_order(order_entity)
        return JsonResponse({"message": "Success"})

    return JsonResponse({"message": "Method Not Allowed"})

@staff_member_required
def sync(request):
    keys = RazorpayKeys.objects.first()
    payment = RazorpayPayments(keys.api_key, keys.api_secret)
    invoices = Invoice.objects.all()
    for invoice in invoices:
        invoice_details = payment.fetch_invoices(invoice.invoice_id)
        invoice.status = invoice_details['status']
        invoice.save()
        if invoice.status == 'paid':
            orders = Order.objects.filter(order_id=invoice_details['order_id'])
            if len(orders) == 0:
                order_details = payment.fetch_orders(
                    invoice_details['order_id'])
                payment.save_order(order_details)
            if invoice_details['payment_id']:
                payments = Payment.objects.filter(payment_id=invoice_details['payment_id'])
                if len(payments) == 0:
                    payment_details = payment.fetch_payment(invoice_details['payment_id'])
                    payment.save_payment(payment_details)

    return JsonResponse({"message": "synced"})

@staff_member_required
def payment_dashboard(request):
    payment_breakdown = {
        'Total Tickets': 0,
        'Conference Only': 0,
        'Conference & Devsprint': 0,
        'Supporter': 0,
    }

    user_tickets = UserTicket.objects.all()
    for user_ticket in user_tickets:
        invoice_id = user_ticket.invoice
        if invoice_id != '0':
            invoice = Invoice.objects.get(invoice_id=invoice_id)
            if invoice.status == 'paid':
                payment_breakdown['Total Tickets'] += 1
                if user_ticket.ticket.id == 1:
                    payment_breakdown['Conference Only'] += 1
                elif user_ticket.ticket.id == 2:
                    payment_breakdown['Conference & Devsprint'] += 1
                elif user_ticket.ticket.id == 3:
                    payment_breakdown['Supporter'] += 1

    return JsonResponse({"data": payment_breakdown})
