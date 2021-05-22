from django.urls import include, path
from . import views

urlpatterns = [
    path('',include("lenus_app.urls")),
    path("signup/",views.signup,name="signup" ),
    path("logout/",views.logout_request,name="logout" ),
    path("login/",views.user_login,name="login" ),
    path("profile/",views.profile,name="profile" ),
    path("edit_profile/", views.user_change, name="edit_profile"),
    path("profile_picture/", views.add_pro_pic, name="add_pro_pic"),
    path("change_profile_picture/", views.change_pro_pic, name="change_pro_pic"),
]
