"""Model"""

from django.db import models


# Best practices in models

class ActorQuerySet(models.QuerySet):
    pass


class ActorManager(models.Manager):
    def get_queryset(self):
        return ActorQuerySet(self.model, using=self._db)


class Actor(models.Model):
    login_id = models.CharField(max_length=50, unique=True)
    avatar_url = models.URLField()

    # Static fields
    created_at = models.DateTimeField(auto_now_add=True)
    # Timestamp format = yyyy-MM-dd HH:mm:ss in settings.py

    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"
        ordering = ['-created_at', ]

    def __str__(self):
        return self.login_id


# Best practices in models


class RepositoryQuerySet(models.QuerySet):
    pass


class RepositoryManager(models.Manager):
    def get_queryset(self):
        return RepositoryQuerySet(self.model, using=self._db)


class Repository(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    # Static fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Repository"
        verbose_name_plural = "Repositories"
        ordering = ['-created_at', ]

    def __str__(self):
        return self.name


# Best practices in models

class EventQuerySet(models.QuerySet):
    pass


class EventManager(models.Manager):
    def get_queryset(self):
        return EventQuerySet(self.model, using=self._db)


class Event(models.Model):
    type = models.CharField(max_length=100)
    actor = models.ForeignKey(Actor, related_name='events')
    repo = models.ForeignKey(Repository, related_name='events')

    # Static fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['-created_at', ]

    def __str__(self):
        return '{} - {}'.format(self.actor, self.repo)
