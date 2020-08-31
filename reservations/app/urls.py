from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from app.feedrss import (
    LastShowFeed,
    LocationFeed,
    RepresentationFeed,
    ListFeedRSSView
)
from app.views import authentication, views, show
from app.views.api import (
    ArtistApiView,
    LocationApiView,
    RepresentationApiView,
    ShowApiView,
    ExternalAPI,
    ExternalAPIShowView,
    ListAPIView
)
from app.views.locationList import LocationListView
from app.views.locationCRUD import (
    CreateLocation,
    DeleteLocation,
    UpdateLocation
)
from app.views.locationdetailed import LocationDetailedView
from app.views.payment import ppalreturn, ppalhome, ppalcancel
from app.views.representationCRUD import (
    CreateRepresentation,
    DeleteRepresentation,
    UpdateRepresentation
)
from app.views.reservation import (
    representationDetailView,
    reservationCreateView,
    reservationUpdateView
)
from app.views.showCRUD import CreateShow, DeleteShow, UpdateShow


urlpatterns = [
    # Home page
    url(r'^$', views.home, name='home'),

    # Authentication
    url(r'^register/$', authentication.signup, name='register'),
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name="app/login.html"),
        name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(template_name="app/logout.html"),
        name='logout'),

    # User Profile
    url(r'^profile/$', authentication.ProfileView.as_view(), name='profile'),
    url(r'^profile/update$', authentication.profileUpdate,
        name='profile-update'),

    # Password Change
    url(r'^password/change/$',
        auth_views.PasswordChangeView.as_view(
            template_name="app/password_change_form.html"
        ),
        name='password_change_form'),
    url(r'^password/change/done/$',
        auth_views.PasswordChangeDoneView.as_view(
            template_name="app/password_change_done.html"
        ),
        name='password_change_done'),

    # Password Reset
    url(r'^password/reset/$',
        auth_views.PasswordResetView.as_view(
            template_name="app/password_reset_form.html"
        ),
        name='password_reset'),
    url(r'^password/reset/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name="app/password_reset_done.html"
        ),
        name='password_reset_done'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="app/password_reset_confirm.html"
        ),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="app/password_reset_complete.html"
        ),
        name='password_reset_complete'),

    # Shows
    url(r'^show/$', show.show_list, name='show'),
    url('^show/autocomplete/$', show.autocomplete_show_list, name='autocompleteShow'),
    url(r'^show/create/$', CreateShow, name='ShowCrud'),
    url(r'^show/read/(?P<pk>[0-9]+)/$', show.show_detail,
        name='show_detail_pk'),
    url(r'^show/read/(?P<slug>[a-zA-Z0-9-]+)/$', show.show_detail_slug,
        name='show_detail_slug'),
    url(r'^show/update/(?P<pk>[0-9]+)/$', UpdateShow, name='UpdateShow'),
    url(r'^show/delete/(?P<pk>[0-9]+)/$', DeleteShow, name='DeleteShow'),
    url(r'^show/pull/read/$', show.show_external_api, name='ext-show'),
    url(r'^show/pull/update/$', show.update_show_external_api,
        name='update-ext-show'),

    # Locations
    url(r'^location/$', LocationListView, name='LocationListView'),
    url(r'^location/create/$', CreateLocation, name='CreateLocation'),
    url(r'^location/read/(?P<slug>[a-zA-Z0-9-]+)/$', LocationDetailedView,
        name='LocationPkView_slug'),
    url(r'^location/update/(?P<pk>[0-9]+)/?$', UpdateLocation,
        name='UpdateLocation'),
    url(r'^location/delete/(?P<pk>[0-9]+)/?$', DeleteLocation,
        name='DeleteLocation'),

    # Representations
    url(r'^representation/create/(?P<pk>[0-9]+)/$', CreateRepresentation,
        name='CreateRepresentation'),
    url(r'^representation/read/(?P<pk>[0-9]+)/$', representationDetailView,
        name='representation_detail'),
    url(r'^representation/update/(?P<pk>[0-9]+)/$', UpdateRepresentation,
        name='UpdateRepresentation'),
    url(r'^representation/delete/(?P<pk>[0-9]+)/$', DeleteRepresentation,
        name='DeleteRepresentation'),

    # Reservation
    url(r'^reservation/create/(?P<pk>[0-9]+)/$', reservationCreateView,
        name='reservationupdate'),
    url(r'^reservation/update/(?P<pk>[0-9]+)/$', reservationUpdateView,
        name='reservationdetails'),

    # PayPal
    url(r'^payhome/$', ppalhome, name='homepaypal'),
    url(r'^payhome/(?P<idreservation>[0-9]+)/$', ppalhome,
        name='homepaypalpk'),
    url(r'^paypalreturn/(?P<pk>[0-9]+)/$', ppalreturn, name='paypalreturn'),
    url(r'^paypalcancel/(?P<pk>[0-9]+)/$', ppalcancel, name='paypalcancel'),
    url(r'^paypalveryhardtofind/', include('paypal.standard.ipn.urls')),

    # Rest API
    url(r'^api/artist/$', ArtistApiView.as_view(), name='api_artist'),
    url(r'^api/show/$', ShowApiView.as_view(), name='api_show'),
    url(r'^api/show/pull/cleaned/$', ExternalAPIShowView.as_view(),
        name='ext-api-show'),
    url(r'^api/show/pull/raw/$', ExternalAPI.as_view(),
        name='ext-api-show-2'),
    url(r'^api/representation/$', RepresentationApiView.as_view(),
        name='api_representation'),
    url(r'^api/location/$', LocationApiView.as_view(), name='api_location'),
    url(r'^api/list/$', ListAPIView.as_view(), name='api_list'),

    # RSS Feeds
    url(r'^rss/list/$', ListFeedRSSView.as_view(), name='rss_list'),
    url(r'^rss/show/$', LastShowFeed(), name='rss_show'),
    url(r'^rss/representation/$', RepresentationFeed(),
        name='rss_representation'),
    url(r'^rss/location/', LocationFeed(), name='rss_location'),
]
