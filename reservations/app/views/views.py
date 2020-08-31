import random

from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from app.models.show import Show
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.serializers import serializers 


def home(request):
    """Default test homepage with base-template this method allowed to select 3 random shows
    and put in a list named slugs then put each slug value into a show variable via a get_object_or_404 methode
    to prevent error """
    shows = Show.objects.order_by("?")[:3]
    slugs = []
    for obj in shows:
        slugs.append(obj.slug)
    show1 = get_object_or_404(Show, slug=slugs[0])
    show2 = get_object_or_404(Show, slug=slugs[1])
    show3 = get_object_or_404(Show, slug=slugs[2])
    shows = [ get_object_or_404(Show, slug=slugs[i]) for i in range(3)]
    context = {
        'shows' : shows,
        'show1': show1,
        'show2': show2,
        'show3': show3,
    }
    return render(request, 'app/home.html', context)
