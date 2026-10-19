from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, Ticket
from .serializers import CategorySerializer, TicketSerializer


@login_required
@ensure_csrf_cookie
def dashboard(request):
    return render(request, "tickets/dashboard.html")


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Проверяем, является ли пользователь администратором, персоналом или методистом
        is_admin_or_methodist = (
                user.is_superuser
                or user.is_staff
                or getattr(user, 'role', None) == 'admin'
                or getattr(user, 'role', None) == 'methodist'
        )

        # Если с правами администратора/методиста — показываем вообще все заявки
        if is_admin_or_methodist:
            queryset = Ticket.objects.all().select_related("category", "owner")
        else:
            # Обычный пользователь видит только свои
            queryset = Ticket.objects.filter(owner=user).select_related("category")

        # Фильтрация по статусу, если она передана в параметрах
        status = self.request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)

        return queryset.order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)