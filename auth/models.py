from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from root.models import Base


class UserProfile(Base):

    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(_("first name"), max_length=255)
    last_name = models.CharField(_("last name"), max_length=255, null=True,
                                 blank=True)
    location = models.CharField(_("location"), max_length=255, null=True,
                                blank=True)

    subscribed = models.BooleanField(_("subscribed"),
                                     max_length=255,
                                     default=False)

    website = models.URLField(null=True, blank=True)
    

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def get_name(self):
        raise NotImplementedError
        

    def save(self):
        raise NotImplementedError

    def __str__(self):
        return '(%s) %s %s' % (self.user.username, self.first_name,
                               self.last_name)
