from django.conf.urls import include, url
froom . import views

urlpatterns = [
    url(r'^$', views.post_principalPage),
]
