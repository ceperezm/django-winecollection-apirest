from django.urls import path, include
from rest_framework import routers
from wines import views


router = routers.DefaultRouter()
router.register(r'wines', views.WineViewSet, 'wines')

urlpatterns = [
    path("api/v1/",include(router.urls))
]

# Generate CRUD