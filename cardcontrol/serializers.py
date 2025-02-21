from cardcontrol.models import *
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['user_id', 'card_name', 'card_account', 'end_date', 'is_active']