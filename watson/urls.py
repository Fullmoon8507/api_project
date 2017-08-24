from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.top, name="top"),
    url(r'^_language_translator$', views.language_translator, name="language_translator"),
    url(r'^_tone_analyzer$', views.tone_analyzer, name="tone_analyzer"),
]
