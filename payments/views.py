from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from payments.models import Invoice
from payments.razorpay.razorpay_payments import RazorpayPayments

import json

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'payload' not in data or 'invoice' not in data['payload']:
            return JsonResponse({"message": "Invalid Data"})

        invoice_entity = data['payload']['invoice']['entity']
        order_entity = data['payload']['order']['entity']
        payment_entity = data['payload']['payment']['entity']

        invoice = Invoice.objects.get(invoice_id=invoice_entity['id'])
        invoice.status = invoice_entity['status']
        invoice.save()
        RazorpayPayments.save_payment(payment_entity)
        RazorpayPayments.save_order(order_entity)
        return JsonResponse({"message": "Success"})

    return JsonResponse({"message": "Method Not Allowed"})
