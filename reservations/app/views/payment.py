from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt  # permet de selectionner si on prend un post ou un get en fonction de la vue? 
from paypal.standard.forms import (
    PayPalEncryptedPaymentsForm,
    PayPalPaymentsForm
)

from app.models import *
from django.contrib.auth.decorators import login_required


@login_required
def ppalhome(request, **kwargs):
    """ paypal home """

    idreservation = request.GET.get('idreservation')
    reservation = get_object_or_404(Reservation, pk=idreservation)
    host = request.get_host()

    args = {}

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        "amount": reservation.price,
        "currency_code": "EUR",
        "item_name": reservation.representation.show.title,
        "invoice": reservation.pk,
        "notify_url": 'http://{}{}'.format(host, reverse('paypal-ipn')),
        "return_url": 'http://{}{}'.format(host, reverse('paypalreturn',
                                           kwargs={'pk': reservation.pk})),
        "cancel_return": 'http://{}{}'.format(host, reverse('paypalcancel',
                                              kwargs={'pk': reservation.pk})),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    args['form'] = form

    context = {'reservation': reservation, 'form': form}
    return render(request, 'app/reservationview.html', context)


@csrf_exempt
@login_required
def ppalreturn(request, pk):
    """"paypal return page"""

    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.status = 'Completed'

    reservation.save()

    return render(request, 'app/paypal_return.html',)


@login_required
def ppalcancel(request, pk):
    """paypal cancel page"""

    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.status = 'Cancelled'

    reservation.save()

    return render(request, 'app/paypal_cancel.html',)
