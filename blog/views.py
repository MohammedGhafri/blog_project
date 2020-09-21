from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView
from .models import Post

class HomeView(TemplateView):
    pass
    # template_name='home.html'

class HomePageView(ListView):
    template_name='home.html'
    model = Post

class Detail_View(DetailView):
    template_name='post_detail.html'
    model = Post

