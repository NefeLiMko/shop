from django.contrib import admin
from .models import Category, Product,Themes,Post,Filt


# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
# Модель категории
class FiltAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = {'slug' : ('name', )}

		
# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated','promo','hit','new']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Themes,ThemeAdmin)
admin.site.register(Post)
admin.site.register(Filt,FiltAdmin)