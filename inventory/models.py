import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from symposion.conference.models import Conference

from root.models import Base

class TShirt(Base):
    """ Model to store the different types of tshirt. """

    gender = models.CharField(_("gender"), max_length=255)
    size = models.CharField(_("size"), max_length=5)
    limit = models.PositiveIntegerField(_("limit"), default=0)
    price = models.PositiveIntegerField(_("price"), default=0, db_index=True)
    conference = models.ForeignKey(Conference, verbose_name=_("conference"))

    class Meta:
        verbose_name = _("tshirt")
        verbose_name_plural = _("tshirts")

    def __str__(self):
        return u"%s: %s" % (self.conference.title, self.gender)


class UserTShirt(Base):
    """ Model for maitaining the tshirt order entry for all the Users. """

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("user tshirt")
        verbose_name_plural = _("tshirt")
        ordering = ['-timestamp']

    def __str__(self):
        return u'%s:%s:%s' % (self.user.username, self.tshirt.gender, self.size)
