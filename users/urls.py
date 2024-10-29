from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import UserCreateApiView

app_name = UsersConfig.name


urlpatterns = [
    path("register/", UserCreateApiView.as_view(), name="register"),
    # path("list/", UserListApiView.as_view(), name="list"),
    # path("detail/<int:pk>/", UserRetrieveApiView.as_view(), name="detail"),
    # path("update/<int:pk>/", UserUpdateApiView.as_view(), name="update"),
    # path("delete/<int:pk>/", UserDestroyApiView.as_view(), name="delete"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
