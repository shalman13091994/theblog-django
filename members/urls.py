from django.urls import path
from .views import (UserRegisterView, EditView, PasswordChangeView, Password_SuccessView, 
ShowProfilePageView, EditProfilePageView, CreateProfilePageView)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name ='register'),
    path('edit_profile/', EditView.as_view(), name='edit-profile'),
    
    # to change the django password change we pass argument as template_name
    # path('password/', auth_views.PasswordChangeView.as_view(template_name= 'registration/change-password.html'), name='password'),
   
    path('password/',PasswordChangeView.as_view(), name = 'password'),
    path('password_sucess/',Password_SuccessView, name = 'password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/profile_page/', EditProfilePageView.as_view(),name ='edit-profile-page'),
    path('create_profile_page/', CreateProfilePageView.as_view(),name ='create-profile-page'),
    
]
