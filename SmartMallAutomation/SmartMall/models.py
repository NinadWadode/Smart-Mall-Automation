from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.db.models.functions import datetime


class Product(models.Model):
    ProductPrice = models.IntegerField()
    ProductName = models.CharField(max_length=20)


class Fridgetemp(models.Model):
    FridgeNumber = models.IntegerField()
    FridgeTemperature = models.IntegerField()


class Fridgehumidity(models.Model):
    FridgeNumber = models.IntegerField()

    FridgeHumidity = models.IntegerField()


class Fridge(models.Model):
    FridgeNumber = models.IntegerField()
    ProductID = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True,
                                  related_name='%(class)s_requests_created')
    FridgeQuantity = models.IntegerField(null=True)
    RequiredLimit = models.IntegerField()
    BuyerID = models.ForeignKey('Buyer', on_delete=models.CASCADE, null=True, related_name='%(class)s_requests_created')

    class Meta:
        unique_together = ('BuyerID', 'ProductID',)


class User1(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.BigIntegerField()
    email = models.CharField(max_length=30)
    Flat = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Pincode = models.IntegerField()
    role = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    tag = models.TextField()


class Buyer(models.Model):
    UserID = models.ForeignKey('User1', on_delete=models.CASCADE, null=True, related_name='%(class)s_requests_created')

    BuyerCash = models.IntegerField()
    FridgeStatus = models.ForeignKey('Fridge', on_delete=models.SET_NULL, null=True,
                                     related_name='%(class)s_requests_created')
    Report = models.CharField(max_length=100)
    Blatitude = models.FloatField()
    Blongitude = models.FloatField()


class Seller(models.Model):
    UserID = models.ForeignKey('User1', on_delete=models.CASCADE, null=True, related_name='%(class)s_requests_created')
    SellerCash = models.IntegerField()
    Slatitude = models.FloatField()
    Slongitude = models.FloatField()


class SellerStock(models.Model):
    SellerID = models.ForeignKey('Seller', on_delete=models.SET_NULL, null=True,
                                 related_name='%(class)s_requests_created')
    ProductID = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True,
                                  related_name='%(class)s_requests_created')
    StockQuantity = models.IntegerField()


class Order(models.Model):
    SellerID = models.ForeignKey('Seller', on_delete=models.SET_NULL, null=True,
                                 related_name='%(class)s_requests_created')
    BuyerID = models.ForeignKey('Buyer', on_delete=models.SET_NULL, null=True,
                                related_name='%(class)s_requests_created')
    ProductID = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True,
                                  related_name='%(class)s_requests_created')
    SellerStockID = models.ForeignKey('SellerStock', on_delete=models.SET_NULL, null=True,
                                      related_name='%(class)s_requests_created')
    OrderQuantity = models.IntegerField()
    OrderPrice = models.IntegerField()

    class Meta:
        unique_together = ('SellerID', 'BuyerID', 'ProductID', 'SellerStockID',)


class Parking(models.Model):
    field = models.IntegerField()
    dist = models.FloatField()

    class Meta:
        db_table = 'parking'


class Fingerenter(models.Model):
    fingernumber = models.IntegerField()
    inn = models.IntegerField()
    time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'fingerenter'


class Dustbin(models.Model):
    status = models.IntegerField()
    location = models.TextField()

    class Meta:
        db_table = 'dustbinstatus'


class Token(models.Model):
    tagid = models.TextField()
    weight = models.FloatField()

    class Meta:
        db_table = 'dustbintoken'

class Cart(models.Model):
    scannerid = models.IntegerField()
    productid = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    

    class Meta:
        db_table = 'cart'
