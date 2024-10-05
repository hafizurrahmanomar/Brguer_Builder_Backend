from django.urls import path
# forJWT=> Jason Web Token
from rest_framework_simplejwt.views import( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,)

from rest_framework.routers import DefaultRouter

from BurgerApi.views import UserProfileViewSet, OrderViewSet


router = DefaultRouter()  

# Register our viewset with the router
router.register(r'user', UserProfileViewSet)  
router.register(r'order', OrderViewSet,basename="order")  

urlpatterns = [
    # forJWT=> Jason Web Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
      
    
] + router.urls
