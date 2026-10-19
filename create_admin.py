import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# 1. Данные суперпользователя
ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'admin@example.com'
ADMIN_PASSWORD = 'admin12345678'

# 2. Данные обычного пользователя
USER_USERNAME = 'user1'
USER_EMAIL = 'user1@example.com'
USER_PASSWORD = 'user123'

# Создание суперпользователя
if not User.objects.filter(username=ADMIN_USERNAME).exists():
    User.objects.create_superuser(ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD)
    print(f"Superuser '{ADMIN_USERNAME}' created successfully!")
else:
    print(f"Superuser '{ADMIN_USERNAME}' already exists.")

# Создание обычного пользователя
if not User.objects.filter(username=USER_USERNAME).exists():
    User.objects.create_user(USER_USERNAME, USER_EMAIL, USER_PASSWORD)
    print(f"Regular user '{USER_USERNAME}' created successfully!")
else:
    print(f"Regular user '{USER_USERNAME}' already exists.")