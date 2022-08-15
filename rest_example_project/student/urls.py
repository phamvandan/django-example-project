from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
# router.register(r'students', views.StudentViewSet,basename="students")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]