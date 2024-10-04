
# from rest_framework import serializers

from rest_framework.serializers import ModelSerializer

from BurgerApi.models import UserProfile

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model=UserProfile
        fields = ('id', 'email','password',)
        
        extra_kwargs={
            'password': {'write_only': True,'style':{
                'input_type': 'password',
                'placeholder': 'Password'}},
            # 'email': {'required': True},
        }
        
        def create(self,validate_data):
            return UserProfile.objects.create_user(
                email=validate_data['email'],
                password=validate_data['password'],
                )
            return user