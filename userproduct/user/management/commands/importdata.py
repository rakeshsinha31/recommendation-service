# myapp/management/commands/importdata.py

import pandas as pd
from django.core.management.base import BaseCommand
from user.models import Customer


class Command(BaseCommand):
    help = "Import data from CSV file into SQLite database"

    def handle(self, *args, **options):
        file_path = "/Users/rakeshsinha/work/tasks/cybertrust/userproduct/customers.xlsx"  # Update with the actual path to your CSV file

        try:
            # Read data from CSV file
            data = pd.read_csv(file_path, encoding="latin-1", on_bad_lines="skip")
            # pd.read_csv('ml-100k/u.item', sep='|', names=m_cols , encoding='latin-1')

            print("9999999")

            # Populate the database table
            for _, row in data.iterrows():
                print(row)
                Customer.objects.create(
                    name=row["name"],
                    age=row["age"],
                    gender=row["gender"],
                    location=row["location"],
                    preference=row["preferences"],
                )

            self.stdout.write(self.style.SUCCESS("Data imported successfully."))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
