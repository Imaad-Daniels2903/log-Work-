from datetime import datetime


class log:
    def __init__(
        self, start_time=None, end_time=None, student=None, description=None, date=None
    ) -> None:
        self.start_time: datetime | None = start_time
        self.end_time: datetime | None = end_time
        self.date: datetime | None = date
        self.student: str | None = student
        self.description: str | None = description

    # Setters
    def set_start(self, time: datetime) -> None:
        self.start_time = time

    def set_end(self, time: datetime) -> None:
        self.end_time = time

    def set_description(self, description: str) -> None:
        self.description = description

    def set_student(self, student: str) -> None:
        self.student = student

    def set_date(self, date: datetime) -> None:
        self.date = date

    # Getters
    def get_start(self) -> datetime | None:
        return self.start_time

    def get_end(self) -> datetime | None:
        return self.end_time

    def get_description(self) -> str | None:
        return self.description

    def get_student(self) -> str | None:
        return self.student

    def get_date(self) -> datetime | None:
        return self.date
