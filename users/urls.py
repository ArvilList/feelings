from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^', include('django.contrib.auth.urls'))
]