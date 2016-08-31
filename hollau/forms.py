from models import UserProfile, Lot, Bet, User
from django import forms


class Lot(forms.ModelForm):
    class Meta:
        model = Lot
        fields = ['name, description, start_price, end_date']


class Bet(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ['price']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'groups', 'user_permissions',
                   'password')
