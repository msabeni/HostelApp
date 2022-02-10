from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('signup', views.signup, name = 'signup'),
    path('matron_signup', views.matron_signup_view.as_view(),name='matron_signup')
]
