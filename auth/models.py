from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from root.models import Base


class UserProfile(Base):

    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(_("first name"), max_length=255)
    last_name = models.CharField(_("last name"), max_length=255, null=True,
                                 blank=True)
    contact = models.CharField(_("contact"), max_length=15, null=True,
                               blank=True)
    location = models.CharField(_("location"), max_length=255, null=True,
                                blank=True)
    age_group = models.CharField(_("age group"), max_length=255, null=True,
                                blank=True)
    gender = models.CharField(_("gender"), max_length=255, null=True,
                                blank=True)
    occupation = models.CharField(_("occupation"), max_length=255, null=True,
                                blank=True)
    company = models.CharField(_("company"), max_length=255, null=True,
                                  blank=True)
    company_title = models.CharField(_("company title"), max_length=255, null=True,
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
