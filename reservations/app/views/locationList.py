from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page

from app.models.location import Location


def LocationListView(request):
    """List of locations.

    This will display paginated list of locations and provide a search bar
    """

    locations = Location.objects.all()
    search_term = ''

    if 'search' in request.GET:  # if there is searched term on the url
        search_term = request.GET['search']
        # getting the searched element in the url

        locations = locations.filter(designation__icontains=search_term)

    paginator = Paginator(locations, 10)  # pagination will allow only 5 items
    page = request.GET.get('page')
    locations = paginator.get_page(page)
    return render(request, 'app/locationList.html',
                  {'locations': locations, 'search_term': search_term})
