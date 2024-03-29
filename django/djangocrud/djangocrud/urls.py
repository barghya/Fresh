
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from .api import views

router=routers.DefaultRouter()
router.register('movies', views.MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
