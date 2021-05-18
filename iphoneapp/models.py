from django.db import models

class Admins(models.Model):
    adminemailid = models.CharField(max_length = 50, primary_key = True)
    adminpassword = models.CharField(max_length = 50)
    class Meta:
        db_table='Admins'
        
class Customer(models.Model):
    custname = models.CharField(max_length = 50)
    custemail = models.CharField(max_length = 50, primary_key = True)
    custpassword = models.CharField(max_length = 50)
    custcontact = models.CharField(max_length = 50)
    class Meta:
        db_table='Customer'

class Store(models.Model):
    storeid = models.AutoField(primary_key = True)
    category = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    price = models.FloatField(max_length = 50)
    imagefile = models.FileField(upload_to='media/', null=True, blank='True')
    def __str__(self):
        return self.name + ": " + str(self.imagefile)
    class Meta:
        db_table = 'Store'
        
class Cart(models.Model):
    cartid = models.AutoField(primary_key = True)
    custemailid = models.CharField(max_length = 50)
    storeid = models.IntegerField()
    name = models.CharField(max_length = 50)
    price = models.FloatField(max_length = 50)
    quantity = models.IntegerField()
    totalprice = models.FloatField(max_length = 50)
    class Meta:
        db_table='Cart'
        
class Orders(models.Model):
    orderid = models.AutoField(primary_key = True)
    custemailid = models.CharField(max_length = 50)
    orderdate = models.CharField(max_length = 50)
    totalbill = models.FloatField(max_length = 50)
    class Meta:
        db_table='Orders'