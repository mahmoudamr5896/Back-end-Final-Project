# forms.py
from allauth.account.forms import SignupForm,LoginForm
from django import forms
from .models import Profile, User

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=True)
    last_name = forms.CharField(max_length=30, label='Last Name', required=True)
    email = forms.EmailField(max_length=255, label='Email', required=True)
    mobile = forms.CharField(max_length=11, label='Mobile Phone', required=True)
    profile_picture = forms.ImageField(label='Profile Picture', required=False)
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        # Remove the username field from the form
        del self.fields['username']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.mobile = self.cleaned_data['mobile']
        if 'profile_picture' in self.cleaned_data:
            user.profile_picture = self.cleaned_data['profile_picture']
        user.save()
        return user
    
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthdate', 
                  'facebook_profile',
                  'country',
                  "first_name",
                  "last_name","mobile","profile_picture"]  # Ad
        

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the 'username' field from the form
        self.fields.pop('username', None)
        # Set the label for the 'login' field to 'Email'
        self.fields['login'].label = 'Email'