import sys
import logging
from django.core.management.base import BaseCommand
from django.core.management import call_command

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Command for handling database schema migrations'

    def add_arguments(self, parser):
        parser.add_argument('--database', default='default', help='The database engine to use for migrations')

    def handle(self, *args, **options):
        database = options['database']

        try:
            self.stdout.write("Creating migrations...")
            call_command('makemigrations', database=database)

            self.stdout.write("Applying migrations...")
            call_command('migrate', database=database)

            self.stdout.write(self.style.SUCCESS("Migrations applied successfully."))

        except Exception as e:
            logger.exception("An error occurred during migration: %s", str(e))
            self.stderr.write(self.style.ERROR("Migration failed. Please check the logs for more details."))
