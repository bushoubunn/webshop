#encoding:utf-8
from django.contrib import admin
from .models import Product,Category
from .forms import ProductAdminForm
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display=('name','created_time','updated_time',)
	list_display_links=('name',)
	list_per_page=20
	ordering=['name']
	search_fields=['name','description','meta_keywords','meta_description']
	exclude=('created_time','updated_time')
	prepopulated_fields={'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	form=ProductAdminForm
	list_display=('name','price','old_price','created_time','updated_time',)
	list_display_links=('name',)
	list_per_page=50
	ordering=['-created_time']
	search_fields=['name','description','meta_keywords','meta_description']
	exclude=('created_time','updated_time')
	prepopulated_fields={'slug':('name',)}
	

		

