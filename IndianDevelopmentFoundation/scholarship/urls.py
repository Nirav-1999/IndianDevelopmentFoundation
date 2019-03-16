from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf.urls import url
from django.urls import include, path
from scholarship import views

app_name = "Student"
# router=SimpleRouter()
router = DefaultRouter()
router.register(r"students", views.StudentViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r'^login/',views.LoginApiView.as_view(),name='login'),
]
