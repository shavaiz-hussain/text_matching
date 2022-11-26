import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from django.utils import timezone

from app.models import Key, Value


class Command(BaseCommand):
    help = "Import Data from csv to models"

    def handle(self, *args, **kwargs):
        with open(settings.BASE_DIR / "dummy_data/dummy.csv") as file:
            reader = csv.DictReader(file)
            keys = []
            values = []
            for row in reader:
                try:
                    keys.append(Key(name=row["Key"]))
                    values.append(Value(name=row["Values"]))
                except KeyError:
                    self.stdout.write("There is something wrong with the csv format")

            Key.objects.bulk_create(keys, ignore_conflicts=True)
            Value.objects.bulk_create(values, ignore_conflicts=True)
