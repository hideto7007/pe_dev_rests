from rest_framework import routers, serializers, viewsets
from rest.models.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    """Actorを並列処理化"""

    class Meta:
        model = Actor
        fileds = ['actor_id', 'first_name', 'last_name', 'created_at', 'updated_at']
