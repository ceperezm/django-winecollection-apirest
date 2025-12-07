from django.urls import path, include
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet,'clients')
router.register(r'providers', views.ProviderViewSet,'providers')

urlpatterns = [
    path("api/v1/",include(router.urls)),
    path("api/v1/register/client/", views.ClientRegisterView.as_view(), name="client-register"),
    path("api/v1/register/provider/", views.ProviderRegisterView.as_view(), name="provider-register"),
]
