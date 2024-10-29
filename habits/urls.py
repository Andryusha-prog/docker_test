from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateApiView, HabitDestroyApiView,
                          HabitListApiView, HabitPublicListApiView,
                          HabitRetrieveApiView, HabitUpdateApiView)

app_name = HabitsConfig.name

urlpatterns = [
    path("list/", HabitListApiView.as_view(), name="list"),
    path("public_list/", HabitPublicListApiView.as_view(), name="public_list"),
    path("create/", HabitCreateApiView.as_view(), name="create"),
    path("retrieve/<int:pk>/", HabitRetrieveApiView.as_view(), name="retrieve"),
    path("update/<int:pk>/", HabitUpdateApiView.as_view(), name="update"),
    path("delete/<int:pk>/", HabitDestroyApiView.as_view(), name="delete"),
]
