from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.list_clients, name='list_clients'),
    path('new/', views.new_client, name='new_client'),
    path('update/<int:id>/', views.update_client, name='update_client'),
    path('delete/<int:id>/', views.delete_client, name='delete_client'),
    path('id/', views.list_id, name='list_id'),
    path('new_id/', views.new_id, name='new_id'),
    path('update_id/<int:id>/', views.update_id, name='update_id'),
    path('delete_id/<int:id>/', views.delete_id, name='delete_id'),
]
