from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import profile

# creating the form in much better way in bootstrap

class SignUpForm(UserCreationForm):
    #creating the field --bootstrap applied to this fields only
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length =150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))
   #  password = forms.CharField(max_length =150, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name':'password1', "id":"password1",'type':'password'}))
   #  confirm_password = forms.CharField(max_length = 150, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name':'password2', "id":"password2",'type':'password'}))
     
   # #   <input type="password" name="password2" autocomplete="new-password" required="" id="id_password2">

    class Meta:
       model = User#by default it have 'password1', 'password2'in the usercreationform
       fields = ('username', 'first_name', 'last_name' ,'email') 

    def __init__(self, *args, **kwargs):
          super(SignUpForm, self).__init__(*args, **kwargs)
          self.fields['username'].widget.attrs['class'] = 'form-control'
          self.fields['password1'].widget.attrs['class'] = 'form-control'
          self.fields['password2'].widget.attrs['class'] = 'form-control'
 

# using inspect element we can see the name of the fields in the webpage
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length =150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length = 150, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(max_length = 150, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length = 150, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
         model = User 
         fields = ('username', 'first_name', 'last_name', 'password' ,'email', 'last_login', 'is_superuser', 'is_staff', 
         'is_active', 'date_joined')


class PasswordChangingForm(PasswordChangeForm):
    #creating the field --bootstrap applied to this fields only
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length =150, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length = 150, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    
    class meta:
       model =User
       fields = ('old_password', 'new_password1', 'new_password2' )

class ProfilePageForm(forms.ModelForm):

    bio = forms.CharField(max_length =150, widget=forms.Textarea(attrs={'class': 'form-control'}))
    website_url = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    facebook_url = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    twitter_url = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pinterest_url = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))
  
    
    class Meta:
        model = profile
        fields = ["bio", 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'pinterest_url']
