from django import forms


class UserForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField()

	class Meta:
		fields = ['username','email','password']


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

	class Meta:
		fields = ['username','password']