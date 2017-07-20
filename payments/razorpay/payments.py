import razorpay
import uuid
import time

class RazorpayPayments:

    API_KEY = "rzp_test_4Q6677vvSd1yvQ"
    API_SECRET = "vxPhJxvEPL7bVV3fLllspqlT"
    client = razorpay.Client(auth=(API_KEY, API_SECRET))

    def createInvoice(self, customer, items):

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

