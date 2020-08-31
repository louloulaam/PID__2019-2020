from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page

from app.models.show import Representation
from app.models.location import Location


def LocationDetailedView(request, slug):
    """This function will return a dictionnary with all the representations
    matching the location's slugs got by clicking on location's
    designations."""

    location = get_object_or_404(Location, slug=slug)
    # get the object with the specified slug that will be shown in the URL.

    representation = Representation.objects.all()
    replist = []

    for i in representation:
        if i.location == location:
            # if representation.location = the location with the slug then add it
            replist.append(i)

    return render(request, 'app/locationdetailed.html',
                  {'location': location, 'repdico': replist})
