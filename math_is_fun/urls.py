from django.contrib import admin
from django.urls import path, include

from exercises.views import GameView
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('players/', include('players.urls')),
    path('math/', views.math_operations, name='math_operations'),
    path('exercise/<int:child_id>/<str:operation>/', GameView.as_view(), name='play_game'),


]
