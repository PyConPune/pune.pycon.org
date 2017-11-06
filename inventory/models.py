import uuid

from django.db import models
from django.utils.translation import ugettext as _

from symposion.conference.models import Conference

from cauth.models import EventUser
from root.models import Base


class Tshirt(Base):
    """ Model to store the different types of tshirt. """

    gender = models.CharField(_("gender"), max_length=255)
    size = models.CharField(_("size"), max_length=5)
    limits = models.PositiveIntegerField(_("limits"), default=0)
    price = models.PositiveIntegerField(_("price"), default=0, db_index=True)
    description = models.CharField(_("description"), max_length=255, null=True)
    image_base64_title = models.CharField(_("image title"), max_length=255,
                                          null=True, blank=True)
    image_base64_text = models.TextField(_("image url"), null=True, blank=True)
    conference = models.ForeignKey(Conference, verbose_name=_("conference"))
    is_limit_reached = models.BooleanField(_("limit reached?"), default=False,
                                           db_index=True)
    disabled = models.BooleanField(_("disabled?"), default=False, db_index=True)

    class Meta:
        verbose_name = _("tshirt")
        verbose_name_plural = _("tshirts")

    def __str__(self):
        return u"%s: %s" % (self.gender, self.size)


class UserTshirt(Base):
    """ Model for maitaining the tshirt order entry for all the Users. """

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(EventUser, on_delete=models.CASCADE)
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
    invoice = models.CharField(_('invoice'), max_length=255, default=0)

    class Meta:
        verbose_name = _("user tshirt")
        verbose_name_plural = _("user tshirts")
        ordering = ['-timestamp']

    def __str__(self):
        return u'%s:%s:%s' % (self.user.username, self.tshirt.gender,
                              self.tshirt.size)
