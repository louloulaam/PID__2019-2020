from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse

from app.models.show import Representation


RESERVATION_STATUS = [
    ('Ongoing', 'En cours'),
    ('Completed', 'Terminée'),
    ('Cancelled', 'Annulée'),
]


class Reservation(models.Model):
    """Model definition for Reservation."""

    representation = models.ForeignKey(Representation,
                                       on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="Utilisateur")
    time = models.DateTimeField(auto_now_add=True,
                                verbose_name="Date de réservation")
    seats = models.PositiveIntegerField(verbose_name="Nombre de sièges")
    price = models.FloatField(verbose_name="Prix total (EUR)")
    status = models.CharField(max_length=9, choices=RESERVATION_STATUS,
                              default='Ongoing', verbose_name="Statut")

    class Meta:
        """Meta definition for Reservation."""

        verbose_name = 'Réservation'
        verbose_name_plural = 'Réservations'
        ordering = ['-status', '-time']

    def __str__(self):
        """Unicode representation of Reservation."""

        return """[{}] ({}) Réservation de {}, le {},
               pour {} ({} place(s))""".format(
                self.pk,
                self.status,
                self.user.username,
                self.representation.time,
                self.representation.show.title,
                self.seats
            )

    def save(self, *args, **kwargs):
        """Save method for Reservation.

        Save the representation to substract the amount of booked seats for
        the available seats left of it. This occurs only if the reservation is
        flagged as "Completed".

        Calculate the total reservation price based on the show price and the
        number of seats booked.
        """

        self.representation.save()

        self.price = round(self.representation.show.price * self.seats, 2)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Reservation."""

        return reverse('reservationdetails', kwargs={'pk': self.pk})
