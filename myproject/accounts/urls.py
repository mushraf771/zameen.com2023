from django.urls import path
from .views import SignupView, UserProfileView,PasswordResetView , PasswordResetSendEmailView, UserChangePassword, LoginView
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('loginuser/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView().as_view(), name='profile'),
    path('changepassword/', UserChangePassword.as_view(), name='changepassword'),
    path('password-reset/<uid>/<token>/', PasswordResetView().as_view(), name='passwordreset'),
    path('password-reset-email/', PasswordResetSendEmailView.as_view(),
         name='password-reset-email'),
]
