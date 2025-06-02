from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  ContactView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactView.as_view(), name='contact'),

]
