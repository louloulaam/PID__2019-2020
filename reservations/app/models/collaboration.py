from django.db import models

from app.models.artist import ArtistType
from app.models.show import Show


class Collaboration(models.Model):
    """Model definition for Collaboration."""

    artist_type = models.ForeignKey(ArtistType, on_delete=models.CASCADE,
                                    verbose_name="Type dartiste")
    show = models.ForeignKey(Show, on_delete=models.CASCADE,
                             verbose_name="Spectacle")

    class Meta:
        """Meta definition for Collaboration."""

        verbose_name = 'Collaboration'
        verbose_name_plural = 'Collaborations'
        ordering = ['pk']

    def __str__(self):
        """Unicode representation of Collaboration."""

        return "[{}] Participation de {} {} à {}".format(
                self.pk,
                self.artist_type.artist.firstname,
                self.artist_type.artist.lastname,
                self.show.title
            )

    def get_absolute_url(self):
        """Return absolute url for Collaboration."""
        return ('')  # TODO: Define absolute url + url name

    # TODO: Define custom methods here
