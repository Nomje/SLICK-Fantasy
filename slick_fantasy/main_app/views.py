from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bet
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
# http://localhost:8000
def home(request):
    return HttpResponse("<h1>Home page</h1>")

# http://localhost:8000
def bets(request):
    bets = Bet.objects.all()
    return render(request, "bets.html", {'bets' : bets})

def bets_detail(request, bet_id):
  bets = Bet.objects.get(id=bet_id)
  return render(request, 'bets/detail.html', { 'bets': bets })

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
    