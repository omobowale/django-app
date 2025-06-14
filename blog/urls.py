from . import views
from django.urls import path


urlpatterns = [
    path('feeds/', views.feeds_list, name = 'feeds_list'),    
    path('feeds/<int:id>', views.single_feed, name = 'single_feed'),    
    path('feeds/create', views.create_feed, name = 'create_feed'),        
    path('feeds/edit/<int:id>', views.edit_feed, name = 'edit_feed'),   
    path('feeds/delete/<int:id>', views.delete_feed, name='delete_feed'), 
]