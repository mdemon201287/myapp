# myapp/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'members', views.MemberViewSet)
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('app.urls')),  # Include the app's URL configurations
    path('', TemplateView.as_view(template_name='index.html')),
]
