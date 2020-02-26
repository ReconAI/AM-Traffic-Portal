from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dataset/$', views.DatasetListView.as_view(), name='datasets'),
    url(r'^dataset/(?P<pk>\d+)$', views.DatasetDetailView.as_view(), name='dataset-detail'),
    
    url(r'^edges/$', views.EdgeNodeListView.as_view(), name='edgenodes'),
    url(r'^edge/(?P<pk>\d+)$', views.EdgeNodeDetailView.as_view(), name='edgenode-detail'),
    url(r'^edge/(?P<pk>\d+)/realtime', views.getRealTime),
] 

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]