from django.urls import path
from . import views

urlpatterns = [
  # http://localhost:8000/
  path('', views.home, name='home'),

  # BETS - INDEX & DETAIL
  # http://localhost:8000/bets/
  path('bets/', views.bets, name='bets'),
  # http://localhost:8000/bets/123/
  path('bets/<int:bet_id>/', views.bets_detail, name='detail'),


  # CREATE BET - CRUD
  # http://localhost:8000/bets/create/
  path('bets/create/', views.BetsCreate.as_view(), name='bets_create'),
  # http://localhost:8000/bets/123/update/
  path('bets/<int:pk>/update/', views.BetsUpdate.as_view(), name='bets_update'),
  # http://localhost:8000/bets/123/delete/
  path('bets/<int:pk>/delete/', views.BetsDelete.as_view(), name='bets_delete'),


  # ADD TEAMS TO BET
  # http://localhost:8000/bets/123/assoc_team/123/
  path('bets/<int:bet_id>/assoc_team/<int:team_id>/', views.assoc_team, name="assoc_team"),

  # LIST OF TEAMS
  # http://localhost:8000/teams/
  path('teams/', views.TeamList.as_view(), name='teams_index'),
  # http://localhost:8000/teams/123/
  path('teams/<int:pk>/', views.TeamDetail.as_view(), name='teams_detail'),
  # http://localhost:8000/teams/create/
  path('teams/create/', views.TeamCreate.as_view(), name='teams_create'),
  # http://localhost:8000/teams/123/update/
  path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='teams_update'),
  # http://localhost:8000/teams/123/delete/
  path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='teams_delete'),
  # http://localhost:8000/accounts/signup/
  path('accounts/signup/', views.signup, name='signup'),
]
