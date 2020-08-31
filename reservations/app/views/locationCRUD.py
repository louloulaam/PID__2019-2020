from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import cache_page

from app.models.location import Location
from app.forms.locationForm import LocationForm
from app.permissions.group import group_required


@group_required('Administrateur', 'Moderateur')
def CreateLocation(request):
    """Creating a location

    This will allow creating a location within our app, if we got permissions
    """

    form = LocationForm(request.POST or None)
    # when the user will click at save he will POST contents
    # if there is something in POST create a form with contents if not create an empty form (NONE)

    if form.is_valid():
        form.save()
        return redirect('LocationListView')  # nom de l'url qui correspond à la vue

    return render(request, 'app/locationCRUD.html',
                  {'createLocationform': form})


@group_required('Administrateur', 'Moderateur')
def UpdateLocation(request, pk):
    """ Updating a location

    This will update a location within our app, if we got permissions
    """

    location = Location.objects.get(pk=pk)  # the slug we got on the url
    form = LocationForm(request.POST or None, instance=location)
    # it will allow us to modify filled with the instance of the "pk location"

    if form.is_valid():
        form.save()
        return redirect(location)
        # because of the model get_absolute_url I can access the view of this specific object.

    return render(request, 'app/locationCRUD.html',
                  {'updateLocationform': form})


@group_required('Administrateur', 'Moderateur')
def DeleteLocation(request, pk):
    """Updating a location

    This will update a location within our app, if we got permissions
    """

    location = Location.objects.get(pk=pk)
    if request.method == 'POST':
        # if the user click on the submit button (displayed by the template)
        # he will post and confirm a delete.

        location.delete()
        return redirect('LocationListView')
    return render(request, 'app/deleteLocation.html', {'location': location})
