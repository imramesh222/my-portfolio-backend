# api/management/commands/create_initial_superuser.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Create initial superuser if not exists"

    def handle(self, *args, **options):
        user_model = get_user_model()
        username = "admin"
        email = "ramesh@gmail.com"
        password = "ramesh@222"
        if not user_model.objects.filter(username=username).exists():
            user_model.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS("Superuser created"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))