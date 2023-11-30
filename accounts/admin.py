from django.contrib import admin
from .models import *

# ===> Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    
# ===> Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category"]
    
# ===> Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "product", "status"]
    
# ===> REGISTERING MODELS

admin.site.register(Tag)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
