from django.db import models


class Artist(models.Model):
    """Model definition for Artist."""

    firstname = models.CharField(max_length=60, verbose_name="Prénom")
    lastname = models.CharField(max_length=60, verbose_name="Nom de famille")

    class Meta:

        """Meta definition for Artist."""

        verbose_name = 'Artiste'
        verbose_name_plural = 'Artistes'
        ordering = ['lastname', 'firstname']

    def __str__(self):
        """Unicode representation of Artist."""

        return "[{}] {} {}".format(self.pk, self.firstname, self.lastname)

    def get_absolute_url(self):
        """Return absolute url for Artist."""

        return ('')  # TODO: Define absolute url + url name

    # TODO: Define custom methods here


class Types(models.Model):
    """Model definition for Types."""

    types = models.CharField(max_length=60, verbose_name="Type d'artiste")

    class Meta:
        """Meta definition for Types."""

        verbose_name = 'Type'
        verbose_name_plural = 'Types'
        ordering = ['types']

    def __str__(self):
        """Unicode representation of Types."""

        return "{}".format(self.types)

    def get_absolute_url(self):
        """Return absolute url for Types."""

        return ('')  # TODO: Define absolute url + url name

    # TODO: Define custom methods here


class ArtistType(models.Model):
    """Model definition for ArtistType."""

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    types = models.ForeignKey(Types, on_delete=models.CASCADE,
                              verbose_name="Type d'artiste")

    class Meta:
        """Meta definition for ArtistType."""

        verbose_name = 'Type d\'artiste'
        verbose_name_plural = 'Types d\'artiste'

    def __str__(self):
        """Unicode representation of ArtistType."""

        return "{} {} ({})".format(self.artist.firstname, self.artist.lastname,
                                   self.types)

    def get_absolute_url(self):
        """Return absolute url for ArtistType."""

        return ('')  # TODO: Define absolute url + url name

    # TODO: Define custom methods here
