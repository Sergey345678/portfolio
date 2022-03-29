from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login_user/", views.login_user, name="login_user"),
    path("register_user/", views.register_user, name="register_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path('nail_master_list/', views.nail_master_list, name='nail_master_list'),
    path('nail_master_review_list/<int:nail_master_id>/', views.nail_master_review_list, name='nail_master_review_list'),
    path('add_nail_master/', views.add_nail_master, name='add_nail_master'),
    path('add_review/<int:nail_master_id>/', views.add_review, name='add_review'),
    path('user_appointments/', views.user_appointments, name='user_appointments'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('add_appointment/<int:nail_master_id>/', views.add_appointment, name='add_appointment'),
]