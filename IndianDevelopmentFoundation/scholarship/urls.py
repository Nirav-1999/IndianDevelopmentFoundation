from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf.urls import url
from django.urls import include, path
from .views import StudentViewSet

app_name = "Student"
# router=SimpleRouter()
router = DefaultRouter()
router.register(r"students", StudentViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls)),
]
