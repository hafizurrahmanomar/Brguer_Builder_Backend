
# from rest_framework import serializers

from rest_framework.serializers import ModelSerializer

from .models import UserProfile, Order, Ingredient, CustomerDetails

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model=UserProfile
        fields = ('id', 'email','password',)
        
        extra_kwargs={
            'password': {'write_only': True,'style':{
                'input_type': 'password',
                'placeholder': 'Password'}},
            'email': {'required': True},
        }
        
        def create(self,validate_data):
            return UserProfile.objects.create_user(
                email=validate_data['email'],
                password=validate_data['password'],
                )
            return user
        
        
class IngredientSerializer(ModelSerializer):
    class Meta:
        model =Ingredient
        fields ="__all__"

class CustomerDetailsSerializer(ModelSerializer):
    class Meta:
        model = CustomerDetails
        exclude = ["id",]
        
        
class OrderSerializer(ModelSerializer):
    ingredients =IngredientSerializer()
    customer = CustomerDetailsSerializer()
    
    class Meta:
        model=Order
        exclude=["id",]
    
    
    def create(self, validated_data):
        ingredient_data = validated_data.pop("ingredients")
        customer_data = validated_data.pop("customer")
        ingredients = IngredientSerializer.create(IngredientSerializer(), validated_data=ingredient_data)
        customer = CustomerDetailsSerializer.create(CustomerDetailsSerializer(), validated_data=customer_data)
        order,created =Order.objects.update_or_create(
            ingredients = ingredients,
            customer=customer,
            price =validated_data.pop("price"),
            orderTime =validated_data.pop("orderTime"),
            user =validated_data.pop("user")
            
        )
        
        return order
       