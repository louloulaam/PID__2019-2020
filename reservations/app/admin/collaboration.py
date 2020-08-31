from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Collaboration


class CollaborationResource(resources.ModelResource):
    """Describe how Collaboration resources can be imported or exported"""

    class Meta:
        """Meta definition for CollaborationResource."""

        model = Collaboration
        skip_unchanged = True


class CollaborationAdmin(ImportExportModelAdmin):
    """Collaboration admin register class

    Custom administration form and list.
    Add the import/export buttom on the top of the entry.
    """

    list_display = ('show', 'artist_lastname', 'artist_firstname',
                    'artist_type_display')
    ordering = ('show', 'artist_type')

    list_filter = ('show', 'artist_type')

    fieldsets = (
        ('Information générales', {
            'description': 'Informations générales concernant la \
                collaboration',
            'fields': ('show', 'artist_type')
        }),
    )

    def artist_lastname(self, collaboration):
        """Display the lastname of the artist"""

        return collaboration.artist_type.artist.lastname

    artist_lastname.short_description = 'Nom de famille de l\'artiste'

    def artist_firstname(self, collaboration):
        """Display the firstname of the artist"""

        return collaboration.artist_type.artist.firstname

    artist_firstname.short_description = 'Prénom de l\'artiste'

    def artist_type_display(self, collaboration):
        """Display the firstname of the artist"""

        return collaboration.artist_type.types.types

    artist_type_display.short_description = 'Type d\'artiste'

    resource_class = CollaborationResource


admin.site.register(Collaboration, CollaborationAdmin)
