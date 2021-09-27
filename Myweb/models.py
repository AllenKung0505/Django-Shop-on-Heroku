from django.db import models

# Create your models here.

class User(models.Model):  #會員資料
    u_username = models.CharField(max_length=20,default='')
    u_password = models.CharField(max_length=20,default='')

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.u_username


class Product(models.Model):  #產品列表
    p_name = models.CharField(max_length=10,default='')
    p_price = models.IntegerField(default=0)
    p_image = models.CharField(max_length=100, default='')
    p_description = models.CharField(max_length=200, default='')

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.p_name

class Order(models.Model):  #訂單
    o_customname = models.CharField(max_length=50,default='')
    o_customphone = models.CharField(max_length=50, default='')
    o_customaddress = models.CharField(max_length=100, default='')
    o_subtotal = models.IntegerField(default=0)
    o_shipping = models.IntegerField(default=0)
    o_grandtotal = models.IntegerField(default=0)

    class Meta:
        db_table = 'Order'

    def __str__(self):
        return self.o_customname


class Detail(models.Model):  #訂單明細
    d_order = models.ForeignKey('Order', on_delete=models.CASCADE)
    d_product = models.CharField(max_length=100, default='')
    d_unitprice = models.IntegerField(default=0)
    d_quantity = models.IntegerField(default=0)
    d_total = models.IntegerField(default=0)

    class Meta:
        db_table = 'Detail'

    def __str__(self):
        return self.d_product