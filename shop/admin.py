from django.contrib import admin
from .models import Product, Order, OrderItem, Profile

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')

# Register the Product model with the custom ProductAdmin
admin.site.register(Product, ProductAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status', 'complete')
    list_filter = ('status', 'complete', 'created_at')
    search_fields = ('user__username', 'id')

admin.site.register(Profile, ProfileAdmin)

# Unregister the old Order admin and register the new one
admin.site.unregister(Order)
admin.site.register(Order, OrderAdmin)
