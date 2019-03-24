from django.shortcuts import render
from .models import Tasks
from rest_framework.generics import(ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView,CreateAPIView)
from .serializers import (TaskListSerializer,TaskDetailSerializer,TaskCreateUpdateSerializer)
from rest_framework.filters import OrderingFilter, SearchFilter
# Create your views here.
class TaskListView(ListAPIView):
	queryset = Tasks.objects.all()
	serializer_class = TaskListSerializer
	filter_backends = [OrderingFilter, SearchFilter]
	search_fields = ['name', 'description']

class TaskDetailsView(RetrieveAPIView):
	queryset = Tasks.objects.all()
	serializer_class = TaskDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'taskl_id'

class TaskUpdateView(RetrieveUpdateAPIView):
	queryset = Tasks.objects.all()
	serializer_class = TaskCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'taskl_id'

class TaskDeleteView(DestroyAPIView):
	queryset = Tasks.objects.all()
	serializer_class = TaskDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'taskl_id'

class TaskCreateView(CreateAPIView):
	serializer_class = TaskCreateUpdateSerializer
	
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)