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

        try:
            # Tenta buscar o usuário existente
            user = User.objects.filter(username=username).first()
            
            if user:
                # Se existe, atualiza a senha e garante que é superusuário
                user.set_password(password)
                user.is_superuser = True
                user.is_staff = True
                user.email = email
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Superusuário "{username}" atualizado com sucesso!')
                )
            else:
                # Se não existe, cria novo
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Superusuário "{username}" criado com sucesso!')
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Erro ao criar/atualizar superusuário: {str(e)}')
            )

