import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def add_arguments(self, parser):
            parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **options):
        file_path = options['csv_file']

        try:
            with open(file_path, 'r', encoding='utf=8') as file:
                reader = csv.DictReader(file, delimiter=';')
                Phone.objects.all().delete()

                for row in reader:
                    Phone.objects.create(
                        id=int(row['id']),
                        name=row['name'],
                        price=float(row['price']),
                        image=row['image'],
                        release_date=row['release_date'],
                        lte_exists=bool(row['lte_exists'].lower() == 'true'),
                    )
            self.stdout.write(self.style.SUCCESS('Successfully imported phones'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during import: {str(e)}'))