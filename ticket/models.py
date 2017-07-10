import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from symposion.conference.models import Conference

from root.models import Base


class Ticket(Base):
    """ Model to store the different types of ticket. """

    title = models.CharField(_("name"), max_length=255)
    limit = models.PositiveIntegerField(_("limit"), default=0)
    price = models.PositiveIntegerField(_("price"), default=0, db_index=True)
    conference = models.ForeignKey(Conference, verbose_name=_("conference"))

    class Meta:
        verbose_name = _("ticket")
        verbose_name_plural = _("tickets")

    def __unicode(self):
        return u"%s: %s" % (self.conference.title, self.title)


class UserTicket(Base):
    """ Model for maitaining the ticket entry for all the Users. """

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("user ticket")
        verbose_name_plural = _("user tickets")
        ordering = ['-timestamp']

    def __unicode__(self):
        return u'%s:%s' % (self.user.username, self.ticket.title)

