from django.shortcuts import render

from .models import Squirrel
# Create your views here.

def squirrels_list(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels}
    return render(request, 'sightings/squirrel_list.html', context)
