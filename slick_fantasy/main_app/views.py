from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Bet, Team

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse


# Home Page
# http://localhost:8000/
def home(request):
    return render(request, "home.html")

# Bets Index
# http://localhost:8000/bets/
def bets(request):
    bets = Bet.objects.all()
    return render(request, "bets.html", {
        'bets': bets
        })

# Bets Detail
# http://localhost:8000/bets/123/
def bets_detail(request, bet_id):
    bets = Bet.objects.get(id=bet_id)
    teams_bets_doesnt_have = Team.objects.exclude(id__in=bets.teams.all().values_list('id'))
    return render(request, 'bets/detail.html', {
        'bets': bets,
        'teams': teams_bets_doesnt_have
    })

# Create a New Bet
# http://localhost:8000/bets/create/
class BetsCreate(CreateView):
    model = Bet
    fields = ['name', 'wager']

    def get_success_url(self, **kwargs):
        # http://localhost:8000/bets/123/
        # path('bets/<int:bet_id>/', views.bets_detail, name='detail'),
        return reverse('detail', args=(self.object.id, ))

# Update Bet
# http://localhost:8000/bets/123/update/
class BetsUpdate(UpdateView):
    model = Bet
    # Only allows user to update wager and name
    fields = ['name', 'wager']

    def get_success_url(self, **kwargs):
        # back to details page of bet
        # path('bets/<int:bet_id>/', views.bets_detail, name='detail'),
        return reverse('detail', args=(self.object.id,))

# Delete Bet
# http://localhost:8000/bets/123/delete/
class BetsDelete(DeleteView):
    model = Bet
    success_url = '/bets/'


# List of Teams
# http://localhost:8000/teams/
class TeamList(ListView):
    model = Team

# Team Detail
# http://localhost:8000/teams/123/
class TeamDetail(DetailView):
    model = Team

# Team Create
# http://localhost:8000/teams/create/
class TeamCreate(CreateView):
    model = Team
    fields = '__all__'

# Team Update
# http://localhost:8000/teams/123/update/
class TeamUpdate(UpdateView):
    model = Team
    fields = ['name', 'score']

    def get_success_url(self, **kwargs):
        # back to details page of bet
        # path('teams/<int:pk>/', views.TeamDetail.as_view(), name='teams_detail'),
        return reverse('teams_detail', args=(self.object.id,))

# Team Delete
# http://localhost:8000/teams/112/delete/
class TeamDelete(DeleteView):
    model = Team
    success_url = '/team/'

# Adding Teams to Bet
# http://localhost:8000/bets/123/assoc_team/123/
def assoc_team(request, bet_id, team_id):
    # id = pk
    Bet.objects.get(id=bet_id).teams.add(team_id)
    return redirect('detail', bet_id=bet_id)
    