from django.urls import path
from . import views

urlpatterns = [

    path('math/<int:child_id>/', views.MathMenuView, name='math_operations'),


    path('play/<int:child_id>/<str:operation>/', views.GameView.as_view(), name='play_game'),
]


