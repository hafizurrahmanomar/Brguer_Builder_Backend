from django.urls import path
from rest_framework.routers import DefaultRouter
from BurgerApi.views import UserProfileViewSet

router = DefaultRouter()  # Create a router object

# Register our viewset with the router
router.register(r'user_profile', UserProfileViewSet)  # Endpoint: /user_profile/

urlpatterns = [


] + router.urls
