from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bet, Team

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
import os


# Home Page
# http://localhost:8000/
def home(request):
    return render(request, "home.html")

# Bets Index
# http://localhost:8000/bets/
@login_required
def bets(request):
    bets = Bet.objects.filter(user=request.user)
    return render(request, "bets.html", {
        'bets': bets
        })

# Bets Detail
# http://localhost:8000/bets/123/
@login_required
def bets_detail(request, bet_id):
    bets = Bet.objects.get(id=bet_id)
    teams_bets_doesnt_have = Team.objects.exclude(id__in=bets.teams.all().values_list('id'))
    return render(request, 'bets/detail.html', {
        'bets': bets,
        'teams': teams_bets_doesnt_have
    })

# Create a New Bet
# http://localhost:8000/bets/create/
class BetsCreate(LoginRequiredMixin, CreateView):
    model = Bet
    fields = ['name', 'wager']

    # This inherited method is called when a
  # valid cat form is being submitted
    def form_valid(self, form):
      # Assign the logged in user (self.request.user)
      form.instance.user = self.request.user  # form.instance is the cat
      # Let the CreateView do its job as usual
      return super().form_valid(form)

    def get_success_url(self, **kwargs):
        # http://localhost:8000/bets/123/
        # path('bets/<int:bet_id>/', views.bets_detail, name='detail'),
        return reverse('detail', args=(self.object.id, ))

# Update Bet
# http://localhost:8000/bets/123/update/
class BetsUpdate(LoginRequiredMixin, UpdateView):
    model = Bet
    # Only allows user to update wager and name
    fields = ['name', 'wager']

    def get_success_url(self, **kwargs):
        # back to details page of bet
        # path('bets/<int:bet_id>/', views.bets_detail, name='detail'),
        return reverse('detail', args=(self.object.id,))

# Delete Bet
# http://localhost:8000/bets/123/delete/
class BetsDelete(LoginRequiredMixin, DeleteView):
    model = Bet
    success_url = '/bets/'


# List of Teams
# http://localhost:8000/teams/
class TeamList(LoginRequiredMixin, ListView):
    model = Team

# Team Detail
# http://localhost:8000/teams/123/
class TeamDetail(LoginRequiredMixin, DetailView):
    model = Team

# Team Create
# http://localhost:8000/teams/create/
class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    fields = '__all__'

    success_url = '/teams/'

# Team Update
# http://localhost:8000/teams/123/update/
class TeamUpdate(LoginRequiredMixin, UpdateView):
    model = Team
    fields = ['name', 'score']

    def get_success_url(self, **kwargs):
        # back to details page of bet
        # path('teams/<int:pk>/', views.TeamDetail.as_view(), name='teams_detail'),
        return reverse('teams_detail', args=(self.object.id,))

# Team Delete
# http://localhost:8000/teams/112/delete/
class TeamDelete(LoginRequiredMixin, DeleteView):
    model = Team
    success_url = '/teams/'

# Adding Teams to Bet
# http://localhost:8000/bets/123/assoc_team/123/
@login_required
def assoc_team(request, bet_id, team_id):
    # id = pk
    Bet.objects.get(id=bet_id).teams.add(team_id)
    return redirect('detail', bet_id=bet_id)
    
@login_required    
def remove_team(request, team_pk):
    print('This is team id =========>' + team_id)
    team_object = Team.objects.get(team_pk)
    
    bets = Bet()
    bets.teams.remove(team_object)
    return render(request, "bets.html", {'bets' : bets})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('bets')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
    