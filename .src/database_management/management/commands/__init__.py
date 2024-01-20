from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Database management commands"

    def handle(self, *args, **options):
        self.stdout.write("Available commands:")
        self.stdout.write(" - migrate: Apply database migrations")
        self.stdout.write(" - makemigrations: Create new database migrations")
        self.stdout.write(" - seeddata: Populate the database with seed data")
        self.stdout.write(" - performancemonitor: Monitor database performance")