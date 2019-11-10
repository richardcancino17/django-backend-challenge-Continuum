# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from RestAPI.serializers import EventSerializer, ActorSerializer, \
    ActorProfileUpdateSerializer
from RestAPI.models import Event, Actor
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


# Pylint & PEP8 actived


class EventAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
    queryset = Event.objects.filter(is_active=True)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event = self.perform_create(serializer)
        if event:
            headers = self.get_success_headers(serializer.data)
            return Response({'message': 'Event created!'},
                            status=status.HTTP_201_CREATED,
                            headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class DeleteAllEventsAPIView(generics.DestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

    def destroy(self, request, *args, **kwargs):
        Event.objects.all().delete()
        return Response({'message': 'Events have been deleted!'},
                        status=status.HTTP_200_OK)


class EventsByActorAPIView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        actor_id = self.kwargs.get('actor_id')
        actor = get_object_or_404(Actor.objects.all(), id=actor_id)
        return Event.objects.filter(actor=actor)


class UpdateProfileAPIView(generics.UpdateAPIView):
    serializer_class = ActorSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        actor_id = serializer.validated_data['login_id']
        actor = get_object_or_404(Actor.objects.all(), id=actor_id)
        actor.save()
        return Response({'message': 'Actor updated profile!'},
                        status=status.HTTP_200_OK)


class ListOrderActorAPIView(generics.ListAPIView):
    serializer_class = ActorSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Actor.objects.all().order_by('-events',
                                                '-events__created_at',
                                                'login_id')
        return queryset
