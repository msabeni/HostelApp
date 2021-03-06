from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('signup', views.signup, name = 'signup'),
    path('matron_signup', views.matron_signup_view.as_view(),name='matron_signup'),
    path('student_signup', views.student_signup_view.as_view(),name='student_signup'),
    path('login',views.login_view,name="login_view"),
    path('logout',views.logout,name='logout'),
    path('edit_profile/<int:id>', views.update_profile , name='edit_profile'),
    path('profile',views.profile,name='profile'),
    path('room',views.list_rooms, name='rooms'),
    path('book_room/<int:id>', views.book_room, name='book_room'),
    path('leave_room/<int:id>', views.leave_room, name='leave_room'),
    # path('rooms',views.matron_view , name="rooms"),
    path('get_notified/<int:id>',views.notification,name='notifications'),
    path('waiting_list',views.waiting_list,name='waiting_list'),
    path('announcements',views.announcements,name='announcements'),
    path('post_announcement/<int:id>',views.upload_announcement,name="post_announcement")

]
