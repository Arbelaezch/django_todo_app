from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
import base
from api import views
# import lists


# Because we're using viewsets instead of views, we can automatically generate 
# the URL conf for our API by simply registering the viewsets with a router class. 
# Again, if we need more control over the API URLs we can simply drop down to using 
# regular class-based views, and writing the URL conf explicitly.


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('base.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
