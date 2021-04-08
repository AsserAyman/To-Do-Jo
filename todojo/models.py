from django.db import models

class ToDoItem(models.Model):
    text = models.TextField()