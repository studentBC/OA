"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from app.views import AuthViewSet
from app.views import ProjectListView
from app.views import ProjectDetailView
from app.views import AuditListView
from app.views import SettingListView
from app.views import SettingDetailView

router = routers.DefaultRouter(trailing_slash=False)
router.register("auth", AuthViewSet, basename="auth")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects', ProjectListView.as_view(), name="project-list"),
    path('api/projects/<int:id>', ProjectDetailView.as_view(), name="project-detail"),
    path('api/audits', AuditListView.as_view(), name="audit-list"),
    path('api/settings', SettingListView.as_view(), name="setting-list"),
    path('api/settings/<str:setting_name>',
         SettingDetailView.as_view(), name="setting-detail"),
]

urlpatterns += router.urls
