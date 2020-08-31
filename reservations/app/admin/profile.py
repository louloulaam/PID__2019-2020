from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import UserProfile


class UserProfileResource(resources.ModelResource):
    """Describe how UserProfile resources can be imported or exported"""

    class Meta:
        """Meta definition for UserProfileResource."""

        model = UserProfile
        skip_unchanged = True


class UserProfileAdmin(ImportExportModelAdmin):
    """UserProfile admin register class

    Custom administration form and list.
    Add the import/export buttom on the top of the entry.
    """

    list_display = ('user', 'user_lastname', 'user_firstname', 'language')
    ordering = ('user', 'language')

    list_filter = ('user', 'language')
    search_fields = ('language',)

    fieldsets = (
        ('Information générales', {
            'description': 'Informations générales concernant le profile de \
                l\'utilisateur',
            'fields': ('user', 'language')
        }),
    )

    def user_lastname(self, userprofile):
        """Display the lastname of the user"""

        return userprofile.user.last_name

    user_lastname.short_description = 'Nom de famille de l\'utilisateur'

    def user_firstname(self, userprofile):
        """Display the firstname of the user"""

        return userprofile.user.first_name

    user_firstname.short_description = 'Prénom de l\'utilisateur'


admin.site.register(UserProfile, UserProfileAdmin)
