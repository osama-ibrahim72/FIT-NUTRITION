from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('up', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('', views.signin, name='signin'),
    path('out', views.signout, name='signout'),
]
