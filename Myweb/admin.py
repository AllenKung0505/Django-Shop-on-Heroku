from django.contrib import admin
from Myweb.models import User,Product,Order,Detail

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Detail)