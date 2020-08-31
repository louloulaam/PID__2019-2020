from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Artist, ArtistType, Types


class ArtistResource(resources.ModelResource):
    """Describe how Artist resources can be imported or exported"""

    class Meta:
        """Meta definition for ArtistResource."""

        model = Artist
        skip_unchanged = True


class ArtistAdmin(ImportExportModelAdmin):
    """Artist admin register class

    Custom administration form and list.
    Add the import/export buttom on the top of the entry.
    """

    list_display = ('lastname', 'firstname')
    ordering = ('-lastname', '-firstname', )

    list_filter = ('lastname', 'firstname')
    search_fields = ('firstname', 'lastname')

    fieldsets = (
        ('Information générales', {
            'description': 'Informations générales concernant l\'artiste',
            'fields': ('lastname', 'firstname')
        }),
    )

    resource_class = ArtistResource


admin.site.register(Artist, ArtistAdmin)


class TypesResource(resources.ModelResource):
    """Describe how Type resources can be imported or exported"""

    class Meta:
        """Meta definition for TypeResource."""

        model = Types
        skip_unchanged = True


class TypesAdmin(ImportExportModelAdmin):
    """Types admin register class

    Custom administration form and list.
    Add the import/export buttom on the top of the entry.
    """

    list_display = ('types', )
    ordering = ('types', )

    list_filter = ('types', )
    search_fields = ('types', )

    fieldsets = (
        ('Information générales', {
            'description': 'Informations générales concernant le type pouvant \
                être assigné à un artiste',
            'fields': ('types', )
        }),
    )

    resource_class = TypesResource


admin.site.register(Types, TypesAdmin)


class ArtistTypeResource(resources.ModelResource):
    """Describe how ArtistType resources can be imported or exported"""

    class Meta:
        """Meta definition for ArtistTypeResource."""

        model = ArtistType
        skip_unchanged = True


class ArtistTypeAdmin(ImportExportModelAdmin):
    """ArtistType admin register class

    Custom administration form and list.
    Add the import/export buttom on the top of the entry.
    """

    list_display = ('artist_lastname', 'artist_firstname', 'types')
    ordering = ('types', )

    list_filter = ('types', )

    fieldsets = (
        ('Information générales', {
            'description': 'Informations générales concernant le type \
                d\'artiste',
            'fields': ('types', )
        }),
    )

    def artist_lastname(self, artist_type):
        """Display the lastname of the artist"""

        return artist_type.artist.lastname

    artist_lastname.short_description = 'Nom de famille de l\'artiste'

    def artist_firstname(self, artist_type):
        """Display the firstname of the artist"""

        return artist_type.artist.firstname

    artist_firstname.short_description = 'Prénom de l\'artiste'

    resource_class = ArtistTypeResource


admin.site.register(ArtistType, ArtistTypeAdmin)
