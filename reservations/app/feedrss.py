from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from app.models import Location, Representation, Show


class ListFeedRSSView(TemplateView):
    """ Render a list of all the rss of the reservations project """
    template_name = 'app/rss_list.html'


class LastShowFeed(Feed):
    """RSS Feed definition for Show"""

    title = "Spectacles"
    link = reverse_lazy('rss_show')
    description = "last show on the site"

    def items(self):
        """Feed item definition"""

        return Show.objects.order_by('-date_created') [:3]

    def item_title(self,item):
        """Feed item title"""

        return item.title

    def item_description(self, item):
        """Feed item description"""

        return item.description


class RepresentationFeed(Feed):
    """RSS Feed definition for Representation"""

    title = "Représentations"
    link = reverse_lazy('rss_representation')
    description = "All representation on the site"

    def items(self):
        """Feed item definition"""

        return Representation.objects.order_by('location')

    def item_title(self,item):
        """Feed item title"""

        return item.show.title

    def item_description(self, item):
        """Feed item description"""

        return item.show.description


class LocationFeed(Feed):
    """RSS Feed definition for Location"""

    title = "Localisations"
    link = reverse_lazy('rss_location')
    description = "All location"

    def items(self):
        """Feed item definition"""

        return Location.objects.order_by('locality')

    def item_title(self,item):
        """Feed item title"""

        return item.designation

    def item_description(self, item):
        """Feed item description"""

        return item.address
