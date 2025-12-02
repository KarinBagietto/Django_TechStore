"""
Comando Django para criar superusuário automaticamente
Uso: python manage.py create_admin
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Cria um superusuário com credenciais padrão'

    def handle(self, *args, **options):
        username = 'esdrasreis'
        email = 'reis@.com'
        password = '1234'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'✅ Superusuário "{username}" criado com sucesso!')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'ℹ️  Superusuário "{username}" já existe.')
            )
