from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('socials', socials, name='socials'),
    path('privacy_policy', privacy_policy, name='privacy_policy'),
    path('tos', tos, name='tos'),
]