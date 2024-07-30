from rest_framework import serializers
from mon_api.models import Personne, Player, Manager

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = ['id', 'username', 'password', 'age', 'mail']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'username', 'password', 'age', 'mail', 'score', 'credits']

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'username', 'password', 'age', 'mail', 'department']
