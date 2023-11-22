from django.urls import path
from app1.views import register_item,register_product,list,update,delete,list_product,update_product,delete_product
app_name="app1"
urlpatterns = [
    path(route='',view=register_item,name="register"),
    path(route='list/',view=list,name='list'),
    path(route='list_product/',view=list_product,name='list_product'),
    path(route='update/<int:pk>/',view=update,name='update'),
    path(route='delete/<int:pk>/',view=delete,name='delete'),
    path(route="register_product",view=register_product,name="register_Product"),
    path(route='update_product/<int:pk>/',view=update_product,name='update_product'),
    path(route='delete_product/<int:pk>/',view=delete_product,name='delete_product'),
]
