from rest_framework import serializers

from group.models import Group, GroupStudent


class GroupSerializers(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class GroupStudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = '__all__'
