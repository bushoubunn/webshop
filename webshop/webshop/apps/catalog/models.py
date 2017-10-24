#encoding:utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Category(models.Model):
    name=models.CharField(max_length=50,verbose_name='名称')
    slug=models.SlugField(max_length=50,unique=True,
    	verbose_name='Slug',help_text='根据name生成的,用于生成页面URL,必须是唯一的')
    description=models.TextField(verbose_name='描述')
    is_activate=models.BooleanField(default=True,verbose_name='是否激活')
    meta_keywords=models.CharField(max_length=255,verbose_name='meta关键字',
    	help_text='meta关键词,这样有利于SEO,用逗号分割')
    meta_description=models.CharField(max_length=255,verbose_name='meta描述',help_text='meta 描述')

    created_time=models.DateField(auto_now_add=True,verbose_name='创建时间')
    updated_time=models.DateField(auto_now=True,verbose_name='更新时间')

    class Meta:
        verbose_name='目录'
        db_table='categories'
        ordering=['-created_time']
        verbose_name_plural=verbose_name

    def  __str__(self):
        return self.name

@python_2_unicode_compatible
class Product(models.Model):
    name=models.CharField(max_length=255,unique=True,verbose_name='名称')
    slug=models.SlugField(max_length=255,unique=True,verbose_name='Slug',
		help_text='根据name生成的,用于生成页面URL,必须是唯一')
    brand=models.CharField(max_length=50,verbose_name='品牌')
    sku=models.CharField(max_length=50,verbose_name='计量单位')
    price=models.DecimalField(max_digits=9,decimal_places=2,verbose_name='价格')
    old_price=models.DecimalField(max_digits=9, blank=True,
                                  decimal_places=2, default=0.00, verbose_name='旧价格')
    image=models.ImageField(max_length=50,verbose_name='图片')
    is_activate=models.BooleanField(default=True,verbose_name='是否激活')
    is_bestseller=models.BooleanField(default=False,verbose_name='是否畅销')
    is_recommended=models.BooleanField(default=False,verbose_name='是否推荐')
    quantity=models.IntegerField(verbose_name='数量')
    description=models.TextField(verbose_name='描述')
    meta_keywords=models.CharField(max_length=255,verbose_name='meta关键词',
    	help_text='meta关键词标签,用逗号分割')
    meta_description=models.CharField(max_length=255,verbose_name='meta描述',
    	help_text='meta 描述标签')
    created_time=models.DateField(auto_now_add=True,verbose_name='创建时间')
    updated_time=models.DateField(auto_now=True,verbose_name='更新时间')
    categories=models.ManyToManyField(Category)

    class Meta:
        db_table='products'
        verbose_name='产品'
        verbose_name_plural=verbose_name
        ordering=['-created_time']

    def __str__(self):
        return self.name

    def sale_price(self):
        if self.old_price >self.price:
            return self.price
        else:
            return None


