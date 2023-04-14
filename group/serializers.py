from rest_framework import serializers

from group.models import Group, GroupStudent

class GroupSerializers(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['students'] = GroupSerializers(instance.student_groups.all(), many=True).data
        return representation



class GroupStudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = '__all__'