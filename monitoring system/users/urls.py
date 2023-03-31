from django.urls import path, include
from . import AdminViews, views
from .import UserViews

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', AdminViews.admin_home, name="admin_home"),
    path('add_user/', AdminViews.add_user, name="add_user"),
    path('add_user_save/', AdminViews.add_user_save, name="add_user_save"),
    path('edit_user/<user_id>', AdminViews.edit_user, name="edit_user"),
    path('edit_user_save/', AdminViews.edit_user_save, name="edit_user_save"),
    path('manage_user/', AdminViews.manage_user, name="manage_user"),
    path('delete_user/<user_id>/', AdminViews.delete_user, name="delete_user"),
    path('check_email_exist/', AdminViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', AdminViews.check_username_exist, name="check_username_exist"),
    path('admin_profile/', AdminViews.admin_profile, name="admin_profile"),
    path('admin_profile_update/', AdminViews.admin_profile_update, name="admin_profile_update"),

    path('visit_user_profile/', AdminViews.visit_user_profile, name="visit_user_profile"),
    
    # URSL for Users
    path('user_home/', UserViews.user_home, name="user_home"),
    path('user_profile/', UserViews.user_profile, name="user_profile"),
    path('user_profile_update/', UserViews.user_profile_update, name="user_profile_update"),
]
