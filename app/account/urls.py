from django.urls import path

from account.views import (
    SignUpView,
    ProfileView,
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    # Login and Logout
    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    # Change Password
    path("change-password/", PasswordChangeView.as_view(), name="change_password"),
    # Forget Password
    path("password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
