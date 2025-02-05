from django.urls import path 
from .import views

app_name = 'store'
urlpatterns = [
    path('',views.index,name='home'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/<str:cate_name>',views.category,name='category'),
    path('test/',views.test,name ='test'), 
]
