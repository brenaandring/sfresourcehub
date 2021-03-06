from . import views
from django.urls import path
from .views import contactView, successView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('resources/create/',
         views.ResourceCreate.as_view(),
         name='resources_create'),
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
]
