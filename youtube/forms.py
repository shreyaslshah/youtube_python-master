from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', )
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    email = forms.CharField(label='Email')

class CommentForm(forms.Form):
    text = forms.CharField(label='')
    #video = forms.IntegerField(widget=forms.HiddenInput(), initial=1) 
    
class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    description = forms.CharField(label='Description', max_length=300, widget=forms.Textarea())
    file = forms.FileField()
