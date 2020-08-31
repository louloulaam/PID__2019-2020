from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Reservation


class ReservationResource(resources.ModelResource):
    """Describe how Reservation resources can be imported or exported"""

    class Meta:
        """Reservation admin register class"""

        model = Reservation
        skip_unchanged = True


class ReservationAdmin(ImportExportModelAdmin):
    """Reservation admin register class

    Custom administration form and list.
    Add the import/export buttom on the top of the entry.
    """

    list_display = ('show_name', 'user', 'user_lastname', 'user_firstname',
                    'time', 'seats', 'price', 'status')
    readonly_fields = ['price', 'time']
    ordering = ('status', '-time')
    date_hierarchy = 'time'

    list_filter = ('status', 'user')
    search_fields = ('time', 'seats', 'price', 'status')

    fieldsets = (
        ('Information générales', {
            'description': 'Informations générales concernant la \
                réservation',
            'fields': ('representation', 'user', 'time', 'seats', 'price', 'status')
        }),
    )

    def show_name(self, reservation):
        """Display the name of the show"""

        return reservation.representation.show.title

    show_name.short_description = 'Spectacle'

    def user_lastname(self, userprofile):
        """Display the lastname of the user"""

        return userprofile.user.last_name

    user_lastname.short_description = 'Nom de famille de l\'utilisateur'

    def user_firstname(self, userprofile):
        """Display the firstname of the user"""

        return userprofile.user.first_name

    user_firstname.short_description = 'Prénom de l\'utilisateur'

    resource_class = ReservationResource


admin.site.register(Reservation, ReservationAdmin)
