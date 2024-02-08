from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordResetForm, MyPasswordSetForm, MyChangePasswordForm

urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm),
         name='login'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm),
         name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html",
                                                     form_class=MyPasswordSetForm), name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    path('passwordchange/',
         auth_views.PasswordChangeView.as_view(template_name='changepassword.html', form_class=MyChangePasswordForm,
                                               success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'),
         name='passwordchangedone'),
]