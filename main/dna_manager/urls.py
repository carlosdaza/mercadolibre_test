from django.conf.urls import url
from django.urls import path

from dna_manager.views import ValidateDNASample, GetStatsView

app_name = 'magnitosDNAValidator'

urlpatterns = [
    url(r'^mutant', ValidateDNASample.as_view(), name='mutant'),
    url(r'^stats', GetStatsView.as_view(), name='stats'),
]