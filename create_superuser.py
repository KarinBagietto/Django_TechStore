"""
Script para criar superusuário automaticamente no Render
Execute: python create_superuser.py
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Credenciais do admin
USERNAME = 'esdrasreis'
EMAIL = 'reis@.com'
PASSWORD = '1234'

def create_superuser():
    """Cria o superusuário se ele não existir"""
    if not User.objects.filter(username=USERNAME).exists():
        User.objects.create_superuser(
            username=USERNAME,
            email=EMAIL,
            password=PASSWORD
        )
        print(f'✅ Superusuário "{USERNAME}" criado com sucesso!')
    else:
        print(f'ℹ️  Superusuário "{USERNAME}" já existe.')

if __name__ == '__main__':
    create_superuser()
