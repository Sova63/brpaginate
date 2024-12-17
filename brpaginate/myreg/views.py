from django.contrib.auth import get_user_model, authenticate,login,logout
from django.urls import reverse_lazy,reverse
from django.views.generic import FormView, RedirectView
from .forms import UserForm,LoginForm


class register(FormView):
    template_name = 'myreg/register.html'
    form_class = UserForm
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user_class = get_user_model()
        user = user_class(email=email,username=username)
        user.set_password(password)
        user.save()
        return super().form_valid(form)

class loginView(FormView):
    template_name = 'myreg/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        print(user)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)

class logoutView(RedirectView):

    def get_redirect_url(self, *args,**kwargs):
        logout(self.request)
        return reverse('article_list')

