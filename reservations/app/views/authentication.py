from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView, UpdateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from app.forms.user import (
    UserProfileSignupForm,
    UserProfileUpdateForm,
    UserSignupForm,
    UserUpdateForm
)
from app.models.profile import UserProfile
from app.models.reservation import Reservation


def signup(request):
    """function for signup/register functionality"""

    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        user_profile_form = UserProfileSignupForm(request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.username = user_form.cleaned_data.get('username')
            user_form.first_name = user_form.cleaned_data.get('first_name')
            user_form.last_name = user_form.cleaned_data.get('last_name')
            user_form.email = user_form.cleaned_data.get('email')
            user_form.raw_password = user_form.cleaned_data.get('password1')
            user_form.raw_password2 = user_form.cleaned_data.get('password2')
            user_form.save()

            user_profile \
                = UserProfile.objects.get(user__username=user_form.username)
            user_profile.language \
                = user_profile_form.cleaned_data.get('language')
            user_profile.save()

            return redirect(reverse('home'))
    else:
        user_form = UserSignupForm()
        user_profile_form = UserProfileSignupForm()

    context = {
        'user_form': user_form,
        'user_profile_form': user_profile_form
    }

    return render(request, 'app/signup.html', context)


class ProfileView(LoginRequiredMixin, ListView):
    """User profile View"""

    template_name = 'app/profile.html'
    model = Reservation

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['reservations'] \
            = Reservation.objects.filter(user=self.request.user)

        return context


@login_required
def profileUpdate(request):
    """User update profile view"""

    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        user_profile_update_form \
            = UserProfileUpdateForm(request.POST,
                                    instance=request.user.userprofile)

        if user_update_form.is_valid() and user_profile_update_form.is_valid():
            username = user_update_form.cleaned_data.get('username')
            first_name = user_update_form.cleaned_data.get('first_name')
            last_name = user_update_form.cleaned_data.get('last_name')
            email = user_update_form.cleaned_data.get('email')
            language = user_profile_update_form.cleaned_data.get('language')

            user_update_form.save()
            user_profile_update_form.save()

            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        user_profile_update_form \
            = UserProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'user_update_form': user_update_form,
        'user_profile_update_form': user_profile_update_form,
    }

    return render(request, 'app/profile_update.html', context)
