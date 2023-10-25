from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from account.forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views


# Login View
class LoginView(auth_views.LoginView):
    redirect_authenticated_user = True
    template_name = "login.html"
    # success_url = reverse_lazy("home")
    next_page = "home"


# LogoutView
class LogoutView(auth_views.LogoutView):
    next_page = "home"


# Password change view
class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = "change.html"
    success_url = "home/"


# Password reset view inherit PasswordChangeView
class PasswordResetView(auth_views.PasswordResetView):
    template_name = "reset.html"
    subject_template_name = "reset-subject.txt"
    email_template_name = "reset-email.html"
    success_url = reverse_lazy("password_reset_done")


# Password reset done view
class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "reset-done.html"


# Password reset confirm view
class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "reset-confirm.html"


# Password reset complete view
class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "reset-complete.html"


# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy("home")
    template_name = "profile.html"

    def get(self, request, *args, **kwargs):
        if request.user.id != self.kwargs.get("pk"):
            raise Http404
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.id != self.kwargs.get("pk"):
            raise Http404
        return super().post(request, *args, **kwargs)
