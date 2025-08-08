from django.urls import path
from rest_framework import routers

from .views import (
    AllTasksAPIViewSet, 
    AllCategoryAPIViewSet, 
    CreateTaskAPIView, 
    CreateCategoryAPIView
)

router = routers.DefaultRouter()
router.register(r"tasklist", AllTasksAPIViewSet)
router.register(r"categorylist", AllCategoryAPIViewSet)

urlpatterns = [
    path("createtask/", CreateTaskAPIView.as_view()),
    path("createcategory/", CreateCategoryAPIView.as_view()),
    
]

urlpatterns += router.urls