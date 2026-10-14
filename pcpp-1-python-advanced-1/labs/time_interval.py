class TimeInterval:
    ONE_HOUR_IN_SECONDS = 3600
    ONE_MINUTE_IN_SECONDS = 60

    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    @property
    def total_seconds(self):
        hours_in_seconds = self._hours * self.ONE_HOUR_IN_SECONDS
        minutes_in_seconds = self._minutes * self.ONE_MINUTE_IN_SECONDS

        return hours_in_seconds + minutes_in_seconds + self._seconds

    @classmethod
    def from_seconds(cls, seconds: int):
        hours, remainder = divmod(seconds, cls.ONE_HOUR_IN_SECONDS)
        minutes, seconds = divmod(remainder, cls.ONE_MINUTE_IN_SECONDS)

        return cls(hours, minutes, seconds)

    def __add__(self, other: "TimeInterval | int"):
        if isinstance(other, TimeInterval):
            total_seconds = self.total_seconds + other.total_seconds
        else:
            total_seconds = self.total_seconds + other

        return self.from_seconds(total_seconds)

    def __sub__(self, other: "TimeInterval | int"):
        if isinstance(other, TimeInterval):
            total_seconds = self.total_seconds - other.total_seconds
        else:
            total_seconds = self.total_seconds - other

        return self.from_seconds(total_seconds)

    def __mul__(self, multiplicator: float):
        total_seconds = self.total_seconds * multiplicator
        return self.from_seconds(total_seconds)

    def __str__(self):
        return f"{self._hours:02d}:{self._minutes:02d}:{self._seconds:02d}"


if __name__ == "__main__":
    first_time_interval = TimeInterval(hours=21, minutes=58, seconds=50)
    second_time_interval = TimeInterval(hours=1, minutes=45, seconds=22)

    print(
        f"{first_time_interval} + {second_time_interval} =",
        first_time_interval + second_time_interval,
    )
    print(
        f"{first_time_interval} - {second_time_interval} =",
        first_time_interval - second_time_interval,
    )
    print(
        f"{first_time_interval} * 2 = ",
        first_time_interval * 2,
    )

    print()

    print(
        f"{first_time_interval} + 62 =",
        first_time_interval + 62,
    )
    print(
        f"{first_time_interval} - 62 =",
        first_time_interval - 62,
    )
