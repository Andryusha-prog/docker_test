from rest_framework.exceptions import ValidationError

from habits.models import Habits


class HabitRelatedAward:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        award = value.get(self.field1)
        related_habit = value.get(self.field2)

        if award and related_habit:
            raise ValidationError(
                "Не должно быть заполнено одновременно и поле вознаграждения, "
                "и поле связанной привычки. Можно заполнить только одно из двух полей."
            )


class HabitTimeAction:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time = value.get(self.field)

        if time and time > 120:
            raise ValidationError("Время действия не доолжно превышать 120 секунд")


class HabitRelatedEnjoy:
    def __init__(self, relate):
        self.relate = relate

    def __call__(self, value):
        relate = value.get(self.relate)
        if relate:
            enjoy_obj = Habits.objects.get(pk=relate.pk)
            enjoy = enjoy_obj.is_enjoined
            if not enjoy:
                raise ValidationError(
                    "Связанная привычка должна являться приятной привычкой"
                )


class HabitEnjoyAwardRelate:
    def __init__(self, enjoy, award, related):
        self.enjoy = enjoy
        self.award = award
        self.related = related

    def __call__(self, value):
        enjoy = value.get(self.enjoy)
        award = value.get(self.award)
        relate = value.get(self.related)

        if enjoy and (award or relate):
            raise ValidationError(
                "У связанной привычки не может быть вознаграждения или связанной привычки"
            )


class HabitPeriodic:
    def __init__(self, periodic):
        self.periodic = periodic

    def __call__(self, value):
        # periodic in hours, max = 168 hours
        periodic = value.get(self.periodic)

        if periodic and periodic > 24 * 7:
            raise ValidationError("Привычка не может вполняться реже раза в неделю")
