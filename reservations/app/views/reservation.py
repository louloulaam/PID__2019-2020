from app.models import *
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt  # permet de selectionner si on prend un post ou un get en fonction de la vue? 
from paypal.standard.forms import (
    PayPalEncryptedPaymentsForm,
    PayPalPaymentsForm
)
from app.models.reservation import Reservation
from django.conf import settings
from django.contrib import messages
from decimal import Decimal
from django.contrib.auth.decorators import login_required


@login_required
def representationDetailView(request, pk):
    """Render the Representation DetailView.

    Display all the meta and current informations of a specific Representation
    object gotten by its pk.
    If the objects isn't found, redirects to the 404 view.
    """

    representation = get_object_or_404(Representation, pk=pk)

    template = "app/reservation_view.html"
    context = {"representation": representation}
    return render(request, template, context)


@login_required
def reservationCreateView(request, pk):
    """Create and render a Reservation object Detail View, leading to a
    checkout view.

    Create an 'Ongoing' Reservation object based on the quantity argument,
    the current user and the chosen Representation object gotten by its pk.
    The user can proceed to a Paypal payment or postpone it.
    Redirect the user to a 404 page if the Representation object was not found.
    """

    qty = float(request.GET.get('qty', default=1))
    representation = get_object_or_404(Representation, pk=pk)
    reservation = Reservation.objects.create(representation=representation,
                                             user=request.user, seats=qty)

    template = "app/reservationview.html"
    context = {"reservation": reservation}
    return render(request, template, context)


@login_required
def reservationUpdateView(request, pk):
    """Render a created Reservation object's Detail View.

    If the order is still pending, the user can procceed to the payment.
    Completed or cancelled orders can not be payed, but their details are still
    avaialable in read-only.

    Only the user whom made de reservation is allowed to see the details of it.
    Otherwise, the user will be redirected to his own profile view.

    If the Reservation object doesn't exist, the user will be redirected to a
    404 page.
    """

    reservation = get_object_or_404(Reservation, pk=pk)

    if request.user == reservation.user:
        template = "app/reservationview.html"
        context = {"reservation": reservation}
        return render(request, template, context)
    else:
        return redirect(reverse('profile'))
