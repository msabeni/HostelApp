from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('signup', views.signup, name = 'signup'),
    path('matron_signup', views.matron_signup_view.as_view(),name='matron_signup'),
    path('student_signup', views.student_signup_view.as_view(),name='student_signup'),
    path('login',views.login_view,name="login_view"),
    path('edit_profile/<int:id>', views.update_profile , name='edit_profile'),
    path('profile',views.profile,name='profile')

]
