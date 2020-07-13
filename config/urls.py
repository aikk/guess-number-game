from django.urls import path
from game import views

urlpatterns = [
    path('', views.game, name='current_game'),
    path('new_game/', views.new_game, name='new_game'),
    path('<int:game_id>/', views.game_detail, name='game_detail'),
]
