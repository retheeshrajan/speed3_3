"""speed3_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from tasks.views import(TaskListView,TaskDetailsView,TaskUpdateView,TaskDeleteView,TaskCreateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasklist/',TaskListView.as_view(), name='task-list'),
    path('tasklist/<int:taskl_id>/',TaskDetailsView.as_view(), name='task-detail'),
    path('tasklist/<int:taskl_id>/update/',TaskUpdateView.as_view(), name='task-update'),
    path('tasklist/<int:taskl_id>/delete/',TaskDeleteView.as_view(), name='task-delete'),
    path('tasklist/create/',TaskCreateView.as_view(), name='task-create'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)