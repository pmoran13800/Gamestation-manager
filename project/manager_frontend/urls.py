from django.conf.urls import url
from django.views.generic import TemplateView

from .views import HomeView
from .views.config import GamestationConfigFormView
from .views.logs import LogsView
from .views.bios import BiosListView, BiosUploadJsonView
from .views.roms import RomListView, RomUploadJsonView
from .views.systems import SystemsListView
from .views.monitor import MonitoringView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    
    url(r'^bios/$', BiosListView.as_view(), name='bios'),
    url(r'^bios/upload$', BiosUploadJsonView.as_view(), name='bios-upload'),
    
    url(r'^config/$', GamestationConfigFormView.as_view(), name='config'),
    
    url(r'^monitoring/$', MonitoringView.as_view(), name='monitoring'),
    
    url(r'^logs/$', LogsView.as_view(), name='logs'),
    
    url(r'^systems/$', SystemsListView.as_view(), name='roms-systems'),
    
    url(r'^systems/roms/(?P<system>\w+)/$', RomListView.as_view(), name='roms-list'),
    url(r'^systems/roms/(?P<system>\w+)/upload/$', RomUploadJsonView.as_view(), name='roms-upload'),
]