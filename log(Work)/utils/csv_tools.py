import csv
import datetime as dt

from log import log


class csv_packager:
    def __init__(self, file_path: str | None = None) -> None:
        self.reader = None
        self.writer = None
        self.field_names = []

        if file_path is None or not file_path.endswith(".csv"):
            self.file_path = "data/work_log.csv"

        else:
            self.file_path = file_path

    def create_new_log(self, field_names: list) -> None:
        if not len(field_names) > 0:
            return

        with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
            field_names = [field.title() for field in field_names]
            self.writer = csv.DictWriter(file, fieldnames=field_names).writeheader()
            self.reader = csv.DictReader(file)

    def start_work(self):
        start_time = dt.time
        date = dt.date
        if self.work_logged. or "date" in self.work_logged:
            return

        self.work_logged.s = date
        self.work_logged["start"] = start_time

    def end_work(self):
        student = input("Student name or number: ")
        desciption = input("Session description")
        end_time = dt.time
