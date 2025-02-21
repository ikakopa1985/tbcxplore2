from django.shortcuts import render
from rest_framework import viewsets
from cardcontrol.serializers import *
from cardcontrol.models import *
from django.contrib.auth.models import User



# Create your views here.


class CardViewset(viewsets.ModelViewSet):
    serializer_class = CardSerializer

    def get_queryset(self):
        user_id_received = self.request.query_params["user_id"]

        print(user_id_received)
        all_cards = Card.objects.filter(user__id=user_id_received)
        return all_cards

