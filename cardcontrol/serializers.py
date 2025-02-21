from cardcontrol.models import *
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    card_name = serializers.CharField(read_only=True)
    card_account = serializers.CharField(read_only=True)
    end_date = serializers.DateField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Card
        fields = ['user_id', 'card_name', 'card_account', 'end_date', 'is_active']