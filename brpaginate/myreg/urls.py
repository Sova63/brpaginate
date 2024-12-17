from django.urls import path
from .views import register,loginView,logoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
	path('register/', register.as_view(), name='register'),
	path('login/',loginView.as_view(), name='login'),
	path('logout/',logoutView.as_view(), name='logout'),
]