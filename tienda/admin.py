from django.contrib import admin
from .models import Vinyl, Order, OrderItem

admin.site.register(Vinyl)
admin.site.register(Order)
admin.site.register(OrderItem)
