from django.urls import path
from . import views

urlpatterns = [
   
    path('',  views.home, name='home'),
    # path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('item/<int:item_id>/delete/', views.item_delete, name='item_delete'),
    path('item/<int:item_id>/update/', views.item_update, name='item_update'),
    path('add/', views.add_record, name='add_record'),

]