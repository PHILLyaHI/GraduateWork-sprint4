from django.urls import path
from users.views import *

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("edit_profile/", UserChangeView.as_view(), name="edit_profile"),
]