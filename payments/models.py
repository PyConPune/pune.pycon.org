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
