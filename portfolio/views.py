from django.shortcuts import render
from .models import PortfolioModel


def home(request):
    projects = PortfolioModel.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
