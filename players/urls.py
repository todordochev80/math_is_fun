from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PlayerListView.as_view(), name='player_list'),

    path('create/', views.PlayerCreateView.as_view(), name='player_create'),

    path('edit/<int:pk>/', views.PlayerUpdateView.as_view(), name='player_edit'),

    path('delete/<int:pk>/', views.PlayerDeleteView.as_view(), name='player_delete'),
]