from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Fpo,Dealer

class FpoSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_fpo = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        fpo = Fpo.objects.create(user=user)
        fpo.phone_number=self.cleaned_data.get('phone_number')
        fpo.location=self.cleaned_data.get('location')
        fpo.save()
        return user

class DealerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True) 

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_dealer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        dealer = Dealer.objects.create(user=user)
        dealer.phone_number=self.cleaned_data.get('phone_number')
        dealer.designation=self.cleaned_data.get('designation')
        dealer.save()
        return user

        