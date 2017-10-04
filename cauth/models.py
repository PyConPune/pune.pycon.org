from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _

from root.models import Base

AGE_GROUP_CHOICES = [
    ('1', 'Less than 10'),
    ('2', '11-17'),
    ('3', '18-24'),
    ('4', '25-34'),
    ('5', '35-44'),
    ('6', '45 and over')
]

OCCUPATION_CHOICES = [
    ('W', 'Working Professional'),
    ('S', 'Student'),
    ('U', 'Temporarily Unemployed'),
    ('C', 'Carer'),
    ('R', 'Retired')
]

TSHIRT_SIZE_CHOICES = [
    ('XS', 'Xtra Small'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Xtra Large'),
    ('XXL', 'Double Xtra Large')
]

class EventUser(AbstractUser, Base):
    pass


class UserProfile(Base):

    user = models.OneToOneField(
        EventUser,
        unique=True
    )
    
    first_name = models.CharField(
        _("first name"),
        max_length=255
    )

    last_name = models.CharField(
        _("last name"),
        max_length=255
    )

    contact = models.CharField(
        _("contact"),
        max_length=15
    )

    location = models.CharField(
        _("location"),
        max_length=255,
        null=True,
        blank=True
    )

    age_group = models.CharField(
        _("age group"),
        choices=AGE_GROUP_CHOICES,
        max_length=255
    )

    gender = models.CharField(
        _("gender"),
        max_length=255,
        null=True,
        blank=True
    )

    tshirt_size = models.CharField(
        _("tshirt size"),
        choices=TSHIRT_SIZE_CHOICES,
        max_length=255
    )

    occupation = models.CharField(
        _("occupation"),
        choices=OCCUPATION_CHOICES,
        max_length=1,
        null=True,
        blank=True
    )

    company = models.CharField(
        _("company"),
        max_length=255
    )

    job_title = models.CharField(
        _("job title"),
        max_length=255,
        null=True,
        blank=True)
    website = models.URLField(null=True, blank=True)
    subscribed = models.BooleanField(_("subscribed"), default=False)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def get_name(self):
        raise NotImplementedError

    def __str__(self):
        return '(%s) %s %s' % (self.gender, self.user.username, self.first_name)
