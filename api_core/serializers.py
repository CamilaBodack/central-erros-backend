from rest_framework import serializers
from .models import User, Agent, Group, GroupUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "last_login")


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ("id", "name", "status", "env", "version", "address")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name")


class GroupUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupUser
        fields = ("id", "group_id", "user_id")
