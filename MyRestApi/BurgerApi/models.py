from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager)


# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError("Email must be provided")
        
        email =self.normalize_email(email)
        user=self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self,email,password):
        user=self.create_user(email,password)
        user.is_superuser=True
        user.is_staff =True
        user.save(using=self._db)
        
        return user
        
class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    is_active =models.BooleanField(default=True)
    is_staff =models.BooleanField(default=False)
    
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email

class Ingredient(models.Model):
    salad = models.IntegerField(default=0)
    cheese = models.IntegerField(default=0)
    meat = models.IntegerField(default=0)
    
class CustomerDetails(models.Model):
    deleveryAddress =models.TextField(blank=True)
    phone = models.CharField(max_length=255,blank=True)
    paymentType =models.CharField(max_length=20,blank=True)

class Order(models.Model):
    user =models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    ingredients=models.OneToOneField(Ingredient,on_delete=models.CASCADE,null=True)
    customer = models.OneToOneField(CustomerDetails,on_delete=models.CASCADE,null=True)
    price =models.CharField(max_length=20,blank=False)
    orderTime =models.CharField(max_length=100,blank=False)
    
    def __str__(self):
        return super().user + "Order"