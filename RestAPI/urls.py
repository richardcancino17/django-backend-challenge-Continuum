from django.conf.urls import url
from RestAPI.views import EventAPIView, DeleteAllEventsAPIView, \
    EventsByActorAPIView, UpdateProfileAPIView, ListOrderActorAPIView

urlpatterns = [
    url(r'^event$', DeleteAllEventsAPIView.as_view()),
    url(r'^events$', EventAPIView.as_view()),
    url(r'^events/actors/(?P<actor_id>[\w-]+)$',
        EventsByActorAPIView.as_view()),
    url(r'^actors$', UpdateProfileAPIView.as_view()),
    url(r'^actors-list$', ListOrderActorAPIView.as_view()),

    # TODO: Django rest can't combine method PUT and GET(List)
    # in the same URL, so I changed the url of the endpoint
]
