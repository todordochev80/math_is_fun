from django.urls import path
from . import views

urlpatterns = [

    path('', views.PlayerListView.as_view(), name='player_list'),


    path('create/', views.PlayerCreateView.as_view(), name='player_create'),


    path('update/<int:pk>/', views.PlayerUpdateView.as_view(), name='player_update'),


    path('delete/<int:pk>/', views.PlayerDeleteView.as_view(), name='player_delete'),


    path('scores/', views.ScoreboardView.as_view(), name='scoreboard'),


    path('select/<int:player_id>/', views.select_player, name='select_player'),
]