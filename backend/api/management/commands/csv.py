import csv

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from foodgram.settings import BASE_DIR
from api.models import Ingredient

class Command(BaseCommand):
    help = 'Импорт из .csv в db'

    def handle(self, *args, **options):

        file_path = BASE_DIR / 'data' / 'ingredients.csv'
        #file_name = '/d/Dev/foodgram-project-react/backend/data/'

        with open(f'{file_path}', encoding='utf-8') as file:
            reader = csv.reader(file)
            Ingredient.objects.bulk_create(
                [Ingredient(name=i[0], measurement_unit=i[1]) for i in reader]
            )
            print('Created')
