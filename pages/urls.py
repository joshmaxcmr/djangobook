from django.urls import path
from .views import  PageAccueil, Apropos
urlpatterns = [
path('', PageAccueil.as_view(), name='home'),
path('apropos/', Apropos.as_view(), name='apropos'),
]
