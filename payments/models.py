from django.db import models
from django.utils.translation import ugettext as _

from root.models import Base

class Invoice(Base):
    """Model to store data for the Invoice created"""

    invoice_id = models.CharField(_("invoice_id"), max_length=255)
    receipt_number = models.CharField(_("receipt_number"), max_length=255)
    order_id = models.CharField(_("order_id"), max_length=255)
    status = models.CharField(_("status"), max_length=255)
    payment_id = models.CharField(_("invoice_id"), max_length=255, null=True)
    expire_by = models.CharField(_("expire_by"), max_length=255, null=True)
    issued_at = models.CharField(_("issued_at"), max_length=255)
    paid_at = models.CharField(_("paid_at"), max_length=255, null=True)
    amount = models.PositiveIntegerField(_("amount"), default=0)
    currency = models.CharField(_("currency"), max_length=255)
    short_url = models.CharField(_("short_url"), max_length=255)
    conference = models.PositiveIntegerField(_("conference"), default=0)
    user = models.PositiveIntegerField(_("user"), default=0)


class Payment(Base):
    """Model to store data for the Payment created"""

    payment_id = models.CharField(_("payment_id"), max_length=255)
    amount = models.PositiveIntegerField(_("amount"), default=0)
    currency = models.CharField(_("currency"), max_length=255, null=True)
    status = models.CharField(_("status"), max_length=255, null=True)
    order_id = models.CharField(_("order_id"), max_length=255, null=True)
    invoice_id = models.CharField(_("invoice_id"), max_length=255, null=True)
    international = models.BooleanField(_("international?"), default=False,
                                           db_index=True)
    amount_refunded = models.PositiveIntegerField(_("amount"), default=0)
    refund_status = models.CharField(_("refund_status"), max_length=255, null=True)
    email = models.CharField(_("email"), max_length=255, null=True)
    contact = models.CharField(_("contact"), max_length=15, null=True,
                               blank=True)
    fee = models.PositiveIntegerField(_("fee"), default=0)
    service_tax = models.PositiveIntegerField(_("service_tax"), default=0)
    created_at = models.CharField(_("created_at"), max_length=255, null=True)


class Order(Base):
    """Model to store data for the Order created"""

    order_id = models.CharField(_("order_id"), max_length=255)
    amount = models.PositiveIntegerField(_("amount"), default=0)
    currency = models.CharField(_("currency"), max_length=255, null=True)
    status = models.CharField(_("status"), max_length=255, null=True)
    created_at = models.CharField(_("created_at"), max_length=255, null=True)


class RazorpayKeys(Base):
    """ Model to store Razorpay Keys """

    api_key = models.CharField(_("api key"), max_length=255)
    api_secret = models.CharField(_("api secret"), max_length=255)
