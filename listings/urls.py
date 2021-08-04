from django.conf.urls import url
from . import apis

urlpatterns = [
    url(r'^units/$', apis.AvailableRoomsAPI.as_view(), name='rooms'),

]
