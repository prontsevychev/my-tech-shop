from django.contrib import admin

from . import models


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]


class CartLineInline(admin.TabularInline):
    model = models.CartLine
    extra = 0


class CartAdmin(admin.ModelAdmin):
    inlines = [CartLineInline, ]


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Cart, CartAdmin)
