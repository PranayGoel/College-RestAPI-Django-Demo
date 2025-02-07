from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView
from rest_framework import routers

router=routers.DefaultRouter()
router.register('notice', views.NoticeViewSet)
router.register('student', views.StudentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='api/')),
    
]  