from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('upload', views.upload, name='upload'),
    path('liver', views.liver, name="liver"),
    path('breast', views.breast, name="breast"),
    path('cervical', views.cervical, name="cervical")
]
