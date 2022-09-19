from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # http://localhost:8000/bets/
    path('bets/', views.bets, name='bets'),
    # http://localhost:8000/bets/1/
    path('bets/<int:bet_id>/', views.bets_detail, name='detail'),
    # http://localhost:8000/bets/create/
    path('bets/create/', views.BetsCreate.as_view(), name='bets_create'),
    path('bets/<int:pk>/update/', views.BetsUpdate.as_view(), name='bets_update'),
    path('bets/<int:pk>/delete/', views.BetsDelete.as_view(), name='bets_delete'),
    # http://localhost:8000/cats/2/aassoc_toy/1/
    path('cats/<int:bet_id>/assoc_team/<int:team_id>/',
         views.assoc_team, name="assoc_team"),
    # http://localhost:8000/teams/
    path('teams/', views.TeamList.as_view(), name='teams_index'),
    # http://localhost:8000/teams/1/
    path('teams/<int:pk>/', views.TeamDetail.as_view(), name='teams_detail'),
    # http://localhost:8000/teams/create/
    path('teams/create/', views.TeamCreate.as_view(), name='teams_create'),
    # http://localhost:8000/teams/1/update/
    path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='teams_update'),
    # http://localhost:8000/teams/1/delete/
    path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='teams_delete'),
]
