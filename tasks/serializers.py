from .models import Tasks
from rest_framework import serializers

class TaskListSerializer(serializers.ModelSerializer):
	class Meta:
		model=Tasks
		fields=['name','description']


class TaskDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model=Tasks
		fields='__all__'

class TaskCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Tasks
		fields=['name','description','image']