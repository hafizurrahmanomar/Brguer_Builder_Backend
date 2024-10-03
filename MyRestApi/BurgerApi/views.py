from rest_framework.viewsets import ModelViewSet
from BurgerApi.serializers import UserProfileSerializer
from MyRestApi.BurgerApi.models import UserProfile

# Create your views here.

class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
