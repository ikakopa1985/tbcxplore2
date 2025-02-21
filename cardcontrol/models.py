from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Card(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT, verbose_name=_('User'))
    card_name = models.CharField(max_length=255, verbose_name=_('Card Name'))
    card_account = models.CharField(max_length=255, verbose_name=_('Card Number'))
    end_date = models.DateField(verbose_name=_('end_date'),null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'), null=True, blank=True)