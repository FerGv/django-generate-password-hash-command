"""Generate password hash command."""

# Django
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """Generate a password hash with the provided argument."""

    help = 'Generate a password hash with the provided argument.'

    def add_arguments(self, parser):
        """Define command arguments."""

        parser.add_argument('password', type=str)

    def handle(self, *args, **options):
        """Return the hash for provided password."""

        try:
            password_hash = make_password(options['password'])
            print(password_hash)
        except Exception as e:
            raise CommandError(
                f'An error has ocurred while generating hash. \n{e}'
            )

        self.stdout.write(self.style.SUCCESS('Password hash generated'))
