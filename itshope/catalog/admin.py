from django.contrib import admin
from .models import Product, Videocard, CPU, Display


class ProductInLine(admin.StackedInline):
    model = Videocard


class CPUInLine(admin.StackedInline):
    model = CPU


class DisplayInLine(admin.StackedInline):
    model = Display


class ProductAdmin(admin.ModelAdmin):
    fields = ['image', 'name', 'manufacturer', 'price', 'description', 'available', 'product_type']
    inlines = [ProductInLine, CPUInLine, DisplayInLine]


admin.site.register(Product, ProductAdmin)
