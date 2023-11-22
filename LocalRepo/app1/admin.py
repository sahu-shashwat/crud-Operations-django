from django.contrib import admin
from app1.models import items,product
# Register your models here.
class items_admin(admin.ModelAdmin):
    list_display=['id','name','desc']
admin.site.register(items,items_admin)

class product_admin(admin.ModelAdmin):
    list_display=['pid','name','desc','price','quantity']
admin.site.register(product,product_admin)