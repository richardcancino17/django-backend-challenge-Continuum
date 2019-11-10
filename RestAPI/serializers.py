from rest_framework import serializers
from RestAPI.models import Event, Actor, Repository


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'login_id', 'avatar_url')


class ActorProfileUpdateSerializer(serializers.SerializerMethodField):
    login_id = serializers.CharField()
    avatar_url = serializers.URLField()


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ('id', 'name', 'url')


class EventSerializer(serializers.ModelSerializer):
    actor = ActorSerializer()
    repo = RepositorySerializer()

    class Meta:
        model = Event
        fields = ('id', 'type', 'actor', 'repo', 'created_at')

    def create(self, validated_data):
        actor_data = validated_data.pop('actor')
        repo_data = validated_data.pop('repo')

        actor = Actor.objects.create(**actor_data)
        repo = Repository.objects.create(**repo_data)
        instance = Event.objects.create(actor=actor, repo=repo,
                                        **validated_data)
        return instance
