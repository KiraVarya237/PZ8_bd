import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'admin@example.com'
ADMIN_PASSWORD = 'adminpassword123'

# админ
try:
    admin_user = User.objects.get(username=ADMIN_USERNAME)
    print(f"Пользователь '{ADMIN_USERNAME}' найден, обновляем права...")
except User.DoesNotExist:
    print(f"Пользователь '{ADMIN_USERNAME}' не найден, создаем...")
    try:
        admin_user = User.objects.create_superuser(
            username=ADMIN_USERNAME,
            email=ADMIN_EMAIL,
            password=ADMIN_PASSWORD
        )
    except Exception:
        admin_user = User(username=ADMIN_USERNAME, email=ADMIN_EMAIL)
        admin_user.set_password(ADMIN_PASSWORD)
        admin_user.save()

admin_user.is_superuser = True
admin_user.is_staff = True
admin_user.is_active = True

# Автоматически ищем поле роли/категории в модели accounts и ставим права админа
for field_name in ['role', 'category', 'type', 'group', 'status']:
    if hasattr(admin_user, field_name):
        setattr(admin_user, field_name, 'admin') # или 'administrator' / 'staff'
        print(f"Установлено поле {field_name} = 'admin'")

admin_user.set_password(ADMIN_PASSWORD)
admin_user.save()
print(f"Суперпользователь '{ADMIN_USERNAME}' успешно настроен")


# обычны1 пользователь
USER_USERNAME = 'user1'
USER_EMAIL = 'user1@example.com'
USER_PASSWORD = 'user123'

try:
    regular_user = User.objects.get(username=USER_USERNAME)
except User.DoesNotExist:
    regular_user = User(username=USER_USERNAME, email=USER_EMAIL)
    regular_user.set_password(USER_PASSWORD)
    regular_user.save()

regular_user.is_superuser = False
regular_user.is_staff = False
regular_user.is_active = True

for field_name in ['role', 'category', 'type', 'group', 'status']:
    if hasattr(regular_user, field_name):
        setattr(regular_user, field_name, 'student')
        print(f"Установлено поле {field_name} = 'student'")

regular_user.set_password(USER_PASSWORD)
regular_user.save()
print(f"Обычный пользователь '{USER_USERNAME}' настроен")