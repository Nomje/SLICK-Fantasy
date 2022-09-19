from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# http://localhost:8000
def home(request):
    return HttpResponse("<h1>Home page</h1>")

# http://localhost:8000
def bets(request):
    return render(request, "bets.html")