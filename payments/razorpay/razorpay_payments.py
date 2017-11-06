import razorpay
import uuid
import time

from payments.models import Payment, Order


class RazorpayPayments:

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.client = razorpay.Client(auth=(self.key, self.secret))

    def create_invoice(self, customer, items):

        receipt_id = str(uuid.uuid4().int)[-10:]
        date = int(time.time())
        data = {
          "customer": customer,
          "line_items": items,
          "draft": "0",
          "sms_notify": "1",
          "email_notify": "1",
          "date": date,
          "receipt": receipt_id,
          "type": "link",
          "currency": "INR",
        }

        invoice = self.client.invoice.create(data=data)
        return invoice

    def fetch_invoices(self, invoice_id):

        invoices = self.client.invoice.fetch(invoice_id)
        return invoices

    def fetch_orders(self, order_id):

        orders = self.client.order.fetch(order_id)
        return orders

    def fetch_payment(self, payment_id):

        invoices = self.client.payment.fetch(payment_id)
        return invoices

    @staticmethod
    def save_payment(payment_entity):

        payment = Payment(payment_id=payment_entity['id'])
        payment.amount = payment_entity['amount']
        payment.currency = payment_entity['currency']
        payment.status = payment_entity['status']
        payment.order_id = payment_entity['order_id']
        payment.invoice_id = payment_entity['invoice_id']
        payment.international = payment_entity['international']
        payment.amount_refunded = payment_entity['amount_refunded']
        payment.refund_status = payment_entity['refund_status']
        payment.email = payment_entity['email']
        payment.contact = payment_entity['contact']
        payment.fee = payment_entity['fee']
        payment.service_tax = payment_entity['tax']
        payment.created_at = str(payment_entity['created_at'])
        payment.save()

    @staticmethod
    def save_order(order_entity):

        order = Order(order_id=order_entity['id'])
        order.amount = order_entity['amount']
        order.currency = order_entity['currency']
        order.status = order_entity['status']
        order.created_at = str(order_entity['created_at'])
        order.save()
