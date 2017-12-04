from django.conf.urls import url

from accounts.views import UserListCreateView
from cleanups.views import CleanupListCreateView, CleanupDetailView, LocationListCreateView

urlpatterns = [
    url(r'^cleanups/', CleanupListCreateView.as_view(), name='cleanups'),
    url(r'^cleanups/(?P<pk>[0-9]+)/$', CleanupDetailView.as_view(), name='cleanup-detail'),
    url(r'^locations/', LocationListCreateView.as_view(), name='locations'),
    url(r'^users/', UserListCreateView.as_view(), name='users'),
]
