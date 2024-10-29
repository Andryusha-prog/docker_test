from rest_framework.serializers import ModelSerializer

from habits.models import Habits
from habits.validators import (HabitEnjoyAwardRelate, HabitPeriodic,
                               HabitRelatedAward, HabitRelatedEnjoy,
                               HabitTimeAction)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habits
        fields = "__all__"
        validators = [
            HabitRelatedAward(field1="award", field2="related_habit"),
            HabitTimeAction(field="time_action"),
            HabitRelatedEnjoy(relate="related_habit"),
            HabitEnjoyAwardRelate(
                enjoy="is_enjoined", award="award", related="related_habit"
            ),
            HabitPeriodic(periodic="periodic"),
        ]
