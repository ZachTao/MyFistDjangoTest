from django.contrib import admin
from product.models import Product
from apitest.models import Apis
from apptest.models import Appcase
from webtest.models import Webcase
'''
TabularInline: 这个主要是横向的以表格的形式展示/添加数据 
StackedInline: 这个主要是纵向的形式展示/添加数据
'''


class AppcaseAdmin(admin.ModelAdmin):
    list_display = ['appcasename', 'apptestresult', 'create_time', 'id', 'product']
    model = Appcase
    extra = 1


class WebcaseAdmin(admin.TabularInline):
    list_display = ['webcasename', 'webtestresult', 'create_time', 'id', 'product']
    model = Webcase
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']
    inlines = [AppcaseAdmin, WebcaseAdmin]


class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'product']
    model = Apis
    extra = 1


admin.site.register(Product)
