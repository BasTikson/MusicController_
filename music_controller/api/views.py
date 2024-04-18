from rest_framework import generics
from .serializer import RoomSerializers
from .models import Room


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
