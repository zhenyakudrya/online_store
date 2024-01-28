from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='Zhenya20031997@yandex.ru',
            first_name='admin',
            last_name='adminovich',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('qwerty123')
        user.save()
