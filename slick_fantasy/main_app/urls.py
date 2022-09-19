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
]
