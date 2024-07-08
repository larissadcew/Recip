from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views  

urlpatterns = [
    path('', views.receipts, name='receipts'),
    path('update_receipt/<int:id>/', views.update_receipt, name='update_receipt'),
    path('delete_receipt/<int:id>/', views.delete_receipt, name='delete_receipt'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('pdf/', views.pdf, name='pdf'),
]

