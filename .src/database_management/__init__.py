import django
from django.core.management import call_command
from django.conf import settings


def perform_schema_migrations():
    """
    Function to perform schema migrations.
    """
    django.setup()
    call_command('migrate')


def seed_data():
    """
    Function to seed data into the database.
    """
    django.setup()
    call_command('loaddata', 'seed_data.json')


def configure_database_engine(engine):
    """
    Function to configure the database engine.
    """
    django.setup()
    settings.DATABASES['default']['ENGINE'] = engine