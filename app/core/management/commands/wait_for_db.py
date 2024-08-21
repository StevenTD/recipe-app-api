"""
Django command to wait for database to be avilable
"""
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        pass
