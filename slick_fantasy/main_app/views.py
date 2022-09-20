from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bet, Team
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
# http://localhost:8000
def home(request):
    return render(request, "home.html")

# http://localhost:8000
def bets(request):
    bets = Bet.objects.all()
    return render(request, "bets.html", {'bets' : bets})

def bets_detail(request, bet_id):
  bets = Bet.objects.get(id=bet_id)
  teams_bets_doesnt_have = Team.objects.exclude(id__in=bets.teams.all().values_list('id'))
  return render(request, 'bets/detail.html', { 'bets': bets, 
  'teams' : teams_bets_doesnt_have})

class BetsCreate(CreateView):
  model = Bet
  fields = ['name', 'wager']

  def get_success_url(self, **kwargs):
        # http://127.0.0.1:8000/bets/9
        # path('bets/<int:bet_id>/', views.bets_detail, name='detail'),
        return reverse('detail', args=(self.object.id,))

class BetsUpdate(UpdateView):
  model = Bet
  # Only allows user to update wager and name
  fields = ['name', 'wager']

  def get_success_url(self, **kwargs):
        return reverse('detail', args=(self.object.id,))

class BetsDelete(DeleteView):
  model = Bet
  success_url = '/bets/'

# http://localhost:8000/toys/
class TeamList(ListView):
    model = Team

# http://localhost:8000/team/1/
class TeamDetail(DetailView):
    model = Team


# http://localhost:8000/team/create/
class TeamCreate(CreateView):
    model = Team
    fields = '__all__'


# http://localhost:8000/team/1/update/
class TeamUpdate(UpdateView):
    model = Team
    fields = ['name', 'color']


# http://localhost:8000/team/1/delete/
class TeamDelete(DeleteView):
    model = Team
    fields = []
    success_url = '/teams/'

# http://localhost:8000/cats/2/assoc_toy/1/
def assoc_team(request, bet_id, team_id):
    # id = pk
    # SELECT name FROM cats WHERE id=team
    Bet.objects.get(id=bet_id).teams.add(team_id)
    return redirect('detail', bet_id=bet_id)
    
def remove_team(request, team_pk):
    print('This is team id =========>' + team_id)
    team_object = Team.objects.get(team_pk)
    
    bets = Bet()
    bets.teams.remove(team_object)
    return render(request, "bets.html", {'bets' : bets})
    