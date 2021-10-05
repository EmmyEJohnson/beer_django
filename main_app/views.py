from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Beer
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Beer:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio

beers = [
  Beer("Stella Artois", "https://i.postimg.cc/050Dz3TV/1200px-Stella-Artois-logo-svg.png",
          "Year Round Brew List: Stella Artois Lager, Stella Artois Solstice Lager and Cidre"),
  Beer("Mother Earth",
          "https://i.postimg.cc/9QMd5pNJ/images.jpg", "Year Round Brew List: Cali Creamin/'- Vanilla Cream Ale, Cali Creamsicle - Orange Vanilla Cream Ale, Tierra Madre - Lager, Hop Diggity - Double IPA, Boo Koo - India Pale Ale, Milk Truck - Latte Stout, and Quit Stalin - BBA Russian Imperial Stout"),
  Beer("Grupo Modelo", "https://i.postimg.cc/GmHySpHf/download.jpg",
          "Year Round Brew List: Pacífico, Corona, Modelo Especial, Modelo Light, Modelo Negra, Modelo Reserva, Victoria, Estrella Jalisco, y León"),
  Beer("Green Flash",
          "https://i.postimg.cc/jjfJtk6Q/GF19-Primary-Logo-RGB.png", "Year Round Brew List: Tropical DNA - India Pale Aler, West Coast IPA, Saturhaze IPA, Soul Style IPA"),
  Beer("Stone",
          "https://i.postimg.cc/x1wcx3rk/gargoyle-0.png", "Year Round Brew List: Stone IPA, Stone Buenaveza - Salt & Lime Lager, Stone Delicious IPA, Stone Tangerine Express Hazy IPA, Stone Fear.Movie.Lions Hazy Double IPA, Stone Hazy IPA, Stine Neverending Haze IPA, Stone Dayfall Beligian White, Stone Scorpion Bowl IPA, STone Ruination Double IPA 2.0 Sans Filtre"),
  Beer("The Lost Abbey",
          "https://i.postimg.cc/T1fbkqDj/lost-abbey-celtic-cross.jpg", "Year Round Brew List: Devotion, Farmhouse, Judgement Day, Lost and Found, Red Barn"),
]

class BeerList(TemplateView):
    template_name = "beer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["beers"] = Beer.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["beers"] = Beer.objects.all()
            # default header for not searching 
            context["header"] = "Popular Beers"
        return context

class BeerCreate(CreateView):
    model = Beer
    fields = ['name', 'img', 'bio', 'verified_beer']
    template_name = "beer_create.html"
    # success_url = "/beers/"
    def get_success_url(self):
        return reverse('beer_detail', kwargs={'pk': self.object.pk})

class BeerDetail(DetailView):
    model = Beer
    template_name = "beer_detail.html"

class BeerUpdate(UpdateView):
    model = Beer
    fields = ['name', 'img', 'bio', 'verified_beer']
    template_name = "beer_update.html"
    # success_url = "/beers/"
    def get_success_url(self):
        return reverse('beer_detail', kwargs={'pk': self.object.pk})

class BeerDelete(DeleteView):
    model = Beer
    template_name = "beer_delete_confirm.html"
    success_url = "/beers/"