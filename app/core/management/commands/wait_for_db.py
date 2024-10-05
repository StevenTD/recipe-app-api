import time
import psycopg2
from psycopg2 import OperationalError as Psycopg2OpError
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.conf import settings


class Command(BaseCommand):
    """Django command to wait for the database and
    create it if it doesn't exist."""

    def handle(self, *args, **options):
        """Entry point for command."""
        self.stdout.write('Waiting for database...')
        db_settings = settings.DATABASES['default']
        db_name = db_settings['NAME']

        db_up = False
        while not db_up:
            try:
                # Try to connect to the database
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError) as e:
                if 'does not exist' in str(e):
                    self.stdout.write(
                        f"Database '{db_name}' does not exist, creating it...")
                    self.create_database_if_not_exists(db_settings)
                    db_up = True  # Set db_up to True since we created the DB
                else:
                    self.stdout.write(
                        'Database unavailable, waiting 1 second...')
                    time.sleep(1)
        self.create_database_if_not_exists(db_settings)
        self.stdout.write(self.style.SUCCESS('Database available!'))

    def create_database_if_not_exists(self, db_settings):
        """Create the database if it doesn't exist."""
        db_name = db_settings['NAME']
        db_user = db_settings['USER']
        db_password = db_settings['PASSWORD']
        db_host = db_settings['HOST']
        db_port = db_settings['PORT']

        try:
            # Connect to the 'postgres' database to create the target DB
            conn = psycopg2.connect(
                dbname='postgres',
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port
            )
            conn.autocommit = True
            cursor = conn.cursor()

            # Create the database
            cursor.execute(f'CREATE DATABASE {db_name}')
            self.stdout.write(self.style.SUCCESS(
                f"Database '{db_name}' created successfully."))

        except psycopg2.Error as e:
            self.stderr.write(self.style.ERROR(
                f"Error creating database: {str(e)}"))

        finally:
            if conn:
                conn.close()
