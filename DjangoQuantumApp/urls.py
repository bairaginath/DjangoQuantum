from django.conf.urls import patterns, include, url
from django.contrib import admin

from DjangoQuantumApp.views import LoginView, UserRegister, GetAllUser

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^api/login/$',LoginView.as_view(), name='login'),
    url(r'^api/users/$',UserRegister.as_view(),name='users'),
    url(r'^api/users/all$',GetAllUser.as_view(),name='allUsers'),
    url(r'^api/users/(?P<user_id>[0-9]+)/$',UserRegister.as_view(),name='users'),
)
