from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from habits.models import Habits
from habits.paginators import ListViewPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer
from habits.services import create_periodic_task_for_tg


# Create your views here.
class HabitCreateApiView(CreateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        data_habit = serializer.save()
        data_habit.user = self.request.user
        create_periodic_task_for_tg(self.request.user.email, data_habit)
        data_habit.save()


class HabitListApiView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = ListViewPaginator

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user)


class HabitPublicListApiView(ListAPIView):
    queryset = Habits.objects.filter(is_public=True)
    serializer_class = HabitSerializer


class HabitRetrieveApiView(RetrieveAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitUpdateApiView(UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        data_habit = serializer.save()
        data_habit.save()


class HabitDestroyApiView(DestroyAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]
