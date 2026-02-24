from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.http import Http404

from .models import UserProfile
from .forms import UserUpdateForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def dispatch(self, request, *args, **kwargs):
        # If registration has been disabled via settings, show a friendly page.
        if not getattr(settings, 'REGISTER_ENABLED', True):
            return render(request, 'registration/registration_disabled.html')
        return super().dispatch(request, *args, **kwargs)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'
    login_url = 'login'

    def get_object(self, queryset=None):
        # Get the current user's profile
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        # Provide a sorted list of permission strings for display
        perms = sorted(self.request.user.get_all_permissions())
        context['permissions'] = perms
        return context





@login_required
@require_http_methods(["POST"])
def profile_update_email(request):
    """AJAX endpoint to update the current user's email address."""
    user = request.user
    form = UserUpdateForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": "ok", "email": user.email})
    else:
        return JsonResponse({"status": "error", "errors": form.errors}, status=400)