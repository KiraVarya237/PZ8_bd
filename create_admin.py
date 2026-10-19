import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Данные для администратора
ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'admin@example.com'
ADMIN_PASSWORD = 'admin12345678'

# 1. Находим или создаём администратора
admin_user, created = User.objects.get_or_create(username=ADMIN_USERNAME, defaults={'email': ADMIN_EMAIL})

# Назначаем суперпользователем и персоналом
admin_user.is_superuser = True
admin_user.is_staff = True
admin_user.is_active = True
admin_user.set_password(ADMIN_PASSWORD)

# Если в вашей модели пользователя есть поле роли/категории (например, role, category, status):
# Укажите нужное имя поля и значение для админа (например, 'admin', 'преподаватель' и т.д.)
if hasattr(admin_user, 'role'):
    admin_user.role = 'admin'  # или другое значение вашей роли администратора
elif hasattr(admin_user, 'category'):
    admin_user.category = 'admin'

admin_user.save()
print(f"Администратор '{ADMIN_USERNAME}' успешно обновлен с правами суперпользователя!")

# 2. Данные для обычного пользователя (студента)
USER_USERNAME = 'user1'
USER_EMAIL = 'user1@example.com'
USER_PASSWORD = 'user123'

student_user, created = User.objects.get_or_create(username=USER_USERNAME, defaults={'email': USER_EMAIL})
student_user.set_password(USER_PASSWORD)

if hasattr(student_user, 'role'):
    student_user.role = 'student'
elif hasattr(student_user, 'category'):
    student_user.category = 'student'

student_user.save()
print(f"Пользователь '{USER_USERNAME}' успешно обновлен/создан!")