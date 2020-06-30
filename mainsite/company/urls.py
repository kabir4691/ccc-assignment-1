from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('contact-us/', views.contactUs, name='contact-us'),
  path('contact-us-submit/', views.contactUsSubmit, name='contact-us-submit'),
  path('team/', views.team, name='team')
]