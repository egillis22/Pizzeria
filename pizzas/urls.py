from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizza',views.pizza, name ='pizza'),
    path('toppings/<int:pizza_id>/',views.toppings,name='toppings'),
    path('new_comment/<int:pizza_id>/',views.new_comment, name='new_comment'),
]