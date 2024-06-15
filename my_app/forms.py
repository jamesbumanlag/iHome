from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	 

    

class AddRecordForm(forms.ModelForm):
    
    first_name = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'First Name',
                'class': 'form-control', 
                'label':''
                }
            ))
    
    last_name = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Last Name',
                'class': 'form-control', 
                'label':''
                }
            ))
    age = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Age',
                'class': 'form-control', 
                'label':''
                }
            ))
    gender = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Gender',
                'class': 'form-control', 
                'label':''
                }
            ))
    religion = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Religion',
                'class': 'form-control', 
                'label':''
                }
            ))
    
    house_street = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'House No/Street Name',
                'class': 'form-control', 
                'label':''
                }
            ))
    suburb = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Suburb',
                'class': 'form-control', 
                'label':''
                }
            ))
    state  = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'State',
                'class': 'form-control', 
                'label':''
                }
            ))
    post_code = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Postcode',
                'class': 'form-control', 
                'label':''
                }
            ))
    country = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Country',
                'class': 'form-control', 
                'label':''
                }
            ))
    section = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Section',
                'class': 'form-control', 
                'label':''
                }
            ))
    med_background = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Medical History',
                'class': 'form-control', 
                'label':''
                }
            ))
    contact_first = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'First Name',
                'class': 'form-control', 
                'label':''
                }
            ))
    contact_last =forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Last Name',
                'class': 'form-control', 
                'label':''
                }
            ))
    contact_number = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Contact Number',
                'class': 'form-control', 
                'label':''
                }
            ))
    contact_rel = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Relationship',
                'class': 'form-control', 
                'label':''
                }
            ))
    

    class Meta:
        model = Record
        exclude = ('user',)
    