from django.shortcuts import render

# Create your views here.

family = [
   { 'name': 'Katie', 'species': 'Girl'},
   { 'name': 'Suki', 'species': 'Shiba Inu'},
   { 'name': 'Adam', 'species': 'Boy'},
]

def home(request):
  context = {"name": "Family", "family": family}
  return render(request, "helloworld/home.html", context)

def details(request, familymember):
  # We replace the dash with a space for later ease of use. The dash is there because of the slugify filter.
  context = {"family" : family, "memebername" : familymember}
  return render(request, 'helloworld/details.html', context)