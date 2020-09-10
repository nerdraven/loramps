from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    Ticket, TicketSerializer
)

class TicketListAPI(generics.ListCreateAPIView):
    name = 'All Tickets'
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

class TicketAPI(generics.RetrieveAPIView):
    name = 'Ticket'
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()