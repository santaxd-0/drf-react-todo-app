from django.db import models



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    category_color = models.CharField(max_length=50, null="Black")
    
    def __str__(self):
        return self.name
    
    
class Task(models.Model):
    TASK_INFO = models.TextChoices("TASK_INFO", "DONE PLANNED")
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    date_created = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=TASK_INFO)
    related_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} task"
    