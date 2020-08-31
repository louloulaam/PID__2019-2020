from django.shortcuts import get_object_or_404, render, redirect

from app.forms.representationForm import (
    RepresentationForm,

)
from app.models.show import Show
from app.models.show import Representation
from app.permissions.group import group_required


@group_required('Administrateur', 'Moderateur')
def CreateRepresentation(request, pk):
    """Creating a Representation.

    This view will allow creating a representation within our app if we got
    permissions.
    """

    show = get_object_or_404(Show, pk=pk)
    # getting the id in order to stay in the current Show detailed view, matching the pk

    form = RepresentationForm(request.POST or None)
    # when the user will click at save he will POST contents
    # if there is something in POST create a form with contents if not create an empty form (NONE)

    if form.is_valid():
        # getting the id in order to stay in the current show detailed view, matching the pk
        form.save()

        return redirect(show)  # we'll be redirect again at the current show detailed view.
    else:
        return render(request, 'app/representationCRUD.html',
                      {'CreateRep': form})


@group_required('Administrateur', 'Moderateur')
def UpdateRepresentation(request, pk):
    """Updating a representation.

    This will allow updating a representation
    """

    representation = get_object_or_404(Representation, pk=pk)
    form = RepresentationForm(request.POST or None, instance=representation)
    if form.is_valid():
        show = representation.show  # getting the show matching the current representation.
        form.save()

        return redirect(show)
    else:
        return render(request, 'app/representationCRUD.html',
                      {'UpdateRep': form})


@group_required('Administrateur', 'Moderateur')
def DeleteRepresentation(request, pk):
    """ Deleting a representation

    This will allow deleting a representation"""

    representation = get_object_or_404(Representation, pk=pk)
    show = representation.show  # getting the show matching the current representation.

    if request.method == 'POST':
        # if the user click on the submit button (displayed by the template)
        # he will post and confirm a delete.

        representation.delete()
        return redirect(show)
    else:
        return render(request, 'app/deleteRepresentation.html',
                      {'representation': representation, 'show': show})
