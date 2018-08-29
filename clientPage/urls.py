from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_principalPage),
    #url(r'^nuestros-clientes$',views.post_nuestrosClientesPage),
]
