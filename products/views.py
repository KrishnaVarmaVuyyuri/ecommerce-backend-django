from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer

# 👉 Allow safe (GET) requests for everyone, write access for admins
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.order_by("-created_at")
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
