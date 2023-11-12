from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'nombre', 'apellido', 'password1', 'password2')
        
class AuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')