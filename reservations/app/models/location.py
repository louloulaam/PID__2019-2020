from django.db import models
from django.urls import reverse
from django.utils.text import slugify

import itertools


class Locality(models.Model):
    """Model definition for Locality."""

    postal_code = models.CharField(max_length=6, unique=True,
                                   verbose_name="Code postal")
    locality = models.CharField(max_length=60, unique=True,
                                verbose_name="Localité")

    class Meta:
        """Meta definition for Locality."""

        verbose_name = 'Localité'
        verbose_name_plural = 'Localités'

    def __str__(self):
        """Unicode representation of Locality."""

        return "{} - {}".format(self.postal_code, self.locality)

    def get_absolute_url(self):
        """Return absolute url for Locality."""

        return ('')  # TODO: Define absolute url + url name

    # TODO: Define custom methods here


class Location(models.Model):
    """Model definition for Location."""

    designation = models.CharField(max_length=60,
                                   verbose_name="Nom de l'emplacement")
    slug = models.SlugField(max_length=60, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True,
                               verbose_name="Adresse")
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True,
                                 blank=True, verbose_name="Localité")
    phone = models.CharField(max_length=30, null=True, blank=True,
                             verbose_name="Téléphone")
    website = models.URLField(max_length=255, null=True, blank=True,
                              verbose_name="Site internet")

    class Meta:
        """Meta definition for Location."""

        verbose_name = 'Emplacement'
        verbose_name_plural = 'Emplacements'
        ordering = ['designation']

    def __str__(self):
        """Unicode representation of Location."""

        return "{}".format(self.designation)

    def save(self, *args, **kwargs):
        """Save method for Show.

        Generate a slug based on the title if the show doesn't exist yet.
        """

        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Location."""

        return reverse('LocationPkView_slug', kwargs={'slug': self.slug})

    def _generate_slug(self):
        """Generate a slug based on the designation of the location

        If the slug is already taken, one or two digits will be added at the
        end of the slug and will increment as long as the slug already exist
        until reaching a non-existant result.
        The slug is truncated to 57 character in order to add the unique digits
        at the end of it.
        """

        max_length = self._meta.get_field('slug').max_length - 3
        value = self.designation
        slug_result = slug_original = \
            slugify(value, allow_unicode=False)[:max_length]

        for i in itertools.count(1):
            if not Location.objects.filter(slug=slug_result).exists():
                break
            slug_result = '{}-{}'.format(slug_original, i)

        self.slug = slug_result
