from django.urls import path

from rest_framework.routers import DefaultRouter

from BurgerApi.views import UserProfileViewSet, OrderViewSet


router = DefaultRouter()  

# Register our viewset with the router
router.register(r'user', UserProfileViewSet)  
router.register(r'order', OrderViewSet,basename="order")  

urlpatterns = [
  
    
] + router.urls
