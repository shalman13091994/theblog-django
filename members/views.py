from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from  blog.models import profile #its blogapp's model
from django.shortcuts import get_object_or_404

class ShowProfilePageView(generic.DetailView):
    model = profile
    template_name='registration/user_profile.html'

    
    def get_context_data(self, **kwargs):
        user = profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
    # dont want to grab everything from db just want to take only from that profile user
    #without using get_object_or_404(profile, id = self.kwargs['pk']) it will show all the profile

        user = get_object_or_404(profile, id = self.kwargs['pk'])
        context['page_user'] = user #this context['page_user] we will use it in user_profile.html
        return context
    
class EditProfilePageView(generic.UpdateView):
    model = profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'pinterest_url']
    success_url = reverse_lazy('home')


class CreateProfilePageView(generic.CreateView):
    model = profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    # fields ="__all__"

#if bill id is 7 tat will pass to self and it will go to the form.instance.user = 7 
# so self.request.user.id will be equal to form.user.id

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) #save the form
    

class PasswordChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm #auth.forms
    form_class =  PasswordChangingForm #user defined form
    template_name = 'registration/change-password.html'
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')

def Password_SuccessView(request):
    return render (request, 'registration/password_success.html')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

#add this to base.html
class EditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('home')
 
# to display the current user's data in the profile
    def get_object(self): #to get the data from tat respective logged in user
        return self.request.user


