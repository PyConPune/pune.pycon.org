from django.db import models
from symposion.conference.models import Conference

class UserTicket(models.Model):

    conference = models.ForeignKey(Conference, verbose_name=_("conference"))
    buyer_name = models.CharField(_("name"), max_length=100)
    buyer_email = models.CharField(_("email"), max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = _("ticket")
        verbose_name_plural = _("tickets")
        ordering = ['buyer_name', 'conference']

    def __unicode__(self):
        return u"%s %s" % (self.buyer_name, self.uuid)
