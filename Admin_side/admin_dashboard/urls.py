# admin_dashboard/urls.py
from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('', views.overview, name='overview'),
    path('user_list/', views.user_list, name='users'),
    path('order_list/', views.order_list, name='orders'),
      path('ip_banning/', views.ip_banning, name='ip_banning'),
      path('activity_logs/', views.activity_logs, name='activity_logs'),
      path('staff_list/', views.staff_list, name='staff_list'),
    # Add more paths as needed
]
