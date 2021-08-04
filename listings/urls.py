from django.conf.urls import url
from . import apis

urlpatterns = [
    url(r'^available-rooms/$', apis.AvailableRoomsAPI.as_view(), name='rooms'),

]
