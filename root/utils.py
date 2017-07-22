from django.conf import settings

def validate_year(year):
    """ Validates the year """
    return year == settings.CONFERENCE_YEAR