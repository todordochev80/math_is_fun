from django.contrib import admin
from django.urls import path, include
from progress.views import practice_progress_view

from exercises.views import MathMenuView
from pages import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),

    path('players/', include('players.urls')),
    path('exercise/', include('exercises.urls')),
    path('practice/', practice_progress_view, name='practice_progress'),

]
