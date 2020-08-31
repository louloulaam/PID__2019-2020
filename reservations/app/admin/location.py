from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Location, Locality


class LocationResource(resources.ModelResource):
    """Describe how Location resources can be imported or exported"""

    class Meta:
        """Meta definition for LocationResource."""

        model = Location
        skip_unchanged = True


class LocationAdmin(ImportExportModelAdmin):
    """Location admin register class

    Custom administration form and list.
    Add the import/export buttom on the top of the entry.
    """

    list_display = ('designation', 'locality', 'phone', 'website')
    readonly_fields = ['slug']
    ordering = ('designation', 'locality')

    list_filter = ('locality', 'designation')
    search_fields = ('designation', 'address', 'website')

    fieldsets = (
        ('Information générales', {
            'description': 'Informations générales concernant \
                l\'emplacement',
            'fields': ('designation', 'slug', 'address', 'locality', 'phone',
                       'website')
        }),
    )

    resource_class = LocationResource


admin.site.register(Location, LocationAdmin)


class LocalityResource(resources.ModelResource):
    """Describe how Type resources can be imported or exported"""

    class Meta:
        """Meta definition for LocalityResource."""

        model = Locality
        skip_unchanged = True


class LocalityAdmin(ImportExportModelAdmin):
    """Locality admin register class

    Custom administration form and list.
    Add the import/export buttom on the top of the entry.
    """

    list_display = ('locality', 'postal_code')
    ordering = ('postal_code',)

    list_filter = ('postal_code', 'locality')
    search_fields = ('postal_code', 'locality')

    fieldsets = (
        ('Information générales', {
            'description': 'Informations générales concernant la localité',
            'fields': ('postal_code', 'locality')
        }),
    )

    resource_class = LocalityResource


admin.site.register(Locality, LocalityAdmin)
