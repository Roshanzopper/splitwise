from django.conf.urls import url, include
from htmlapp import views

# Create a router and register our viewsets with it.

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.

app_name = 'htmlapp'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^delete/(?P<id>[0-9]+)/', views.DeleteView, name='delete'),
    url(r'^create/', views.CreateView, name='create'),
    url(r'^save/', views.savenew, name='save'),
]
