from django.urls import path
# forJWT=> Jason Web Token
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
 
)

from rest_framework.routers import DefaultRouter

from .views import UserProfileViewSet


router = DefaultRouter()  # Create a router object

# Register our viewset with the router
router.register(r'user', UserProfileViewSet)  # Endpoint: /user_profile/

urlpatterns = [
    # forJWT=> Jason Web Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
     path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  
    
] + router.urls
