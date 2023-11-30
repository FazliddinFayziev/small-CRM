from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Order)
