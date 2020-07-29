from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    MALE = 'M', _('Male')
    FEMALE = 'F', _('Female')
    NOT_SPECIFIED = 'N', _('Not Specified')

    @classmethod
    def template_choices(cls):
        json_obj = {}
        for value in cls:
            json_obj[value.__dict__.get('_name_')] = value.__dict__.get('_value_')
        return json_obj


class Role(models.IntegerChoices):
    SUPER_ADMIN = 1, _('Super Admin')
    ADMIN = 2, _('Admin')
    STAFF = 3, _('Staff')
    PARTNER = 4, _('Partner')
    FREELANCER = 5, _('Freelancer')
    CUSTOMER = 6, _('Customer')

    @classmethod
    def template_choices(cls):
        json_obj = {}
        for value in cls:
            json_obj[value.__dict__.get('_name_')] = value.__dict__.get('_value_')
        return json_obj


class UserStatus(models.IntegerChoices):
    ACTIVE = 1, _('Active')
    NOT_ACTIVE = 2, _('Not Active')
    BLOCKED = 3, _('Blocked')

    @classmethod
    def template_choices(cls):
        json_obj = {}
        for value in cls:
            json_obj[value.__dict__.get('_name_')] = value.__dict__.get('_value_')
        return json_obj
