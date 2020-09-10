from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .serializers import (
    EventSerializer, TicketSerializer, Event
)

@api_view(['GET'])
def tickets(request, id):
    try:
        event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        event = None
    if event:
        tickets = event.ticket_set.only()
        serialized_ticket = []
        for ticket in tickets:
            data = TicketSerializer(ticket).data
            data.popitem('event_code')
            serialized_ticket.append(data)
        del data
        return Response(serialized_ticket)
    return Response({'message': 'Not Found'}, status=404)


@api_view(['GET'])
def ticket(request, id, ticket):
    try:
        event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        event = None
    if event:
        ticket = event.ticket_set.filter(id=1).first()
        data = TicketSerializer(ticket).data
        data.popitem('event_code')
        return Response(data)
    return Response({'message': 'Not Found'}, status=404)


class EventsAPI(generics.ListCreateAPIView):
    name = 'All Events'
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventAPI(generics.RetrieveAPIView):
    name = 'Event'
    serializer_class = EventSerializer
    queryset = Event.objects.all()