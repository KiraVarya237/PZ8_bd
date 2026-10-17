from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def healthz(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    # Системная проверка здоровья
    path('healthz/', healthz),

    path('admin/', admin.site.urls),

    # Стандартные маршруты авторизации
    path('accounts/', include('django.contrib.auth.urls')),

    # Маршруты приложения accounts
    path('accounts/', include('accounts.urls')),
    path('', include('accounts.urls')),

    # Маршруты приложения tickets
    path('tickets/', include('tickets.urls')),
]