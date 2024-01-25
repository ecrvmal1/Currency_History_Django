from django.urls import path, include
from mainapp import views
from rest_framework.routers import DefaultRouter
from mainapp.views import RateViewSet


router = DefaultRouter()
router.register('get-current-usd', RateViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
