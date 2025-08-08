from rest_framework import generics, viewsets

from .models import (
    Task,
    Category
)
from .serializers import (
    TaskAPISerializer,
    CategoryAPISerializer
)

class AllTasksAPIViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API for list all tasks
    """
    queryset = Task.objects.all()
    serializer_class = TaskAPISerializer

class AllCategoryAPIViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API for list all categories
    """
    queryset = Category.objects.all()
    serializer_class = CategoryAPISerializer
    
class CreateTaskAPIView(generics.CreateAPIView):
    """
    API to create new task
    """
    queryset = Task.objects.all()
    serializer_class = TaskAPISerializer
    
class CreateCategoryAPIView(generics.CreateAPIView):
    """
    API to create new category
    """
    queryset = Category.objects.all()
    serializer_class = CategoryAPISerializer
    