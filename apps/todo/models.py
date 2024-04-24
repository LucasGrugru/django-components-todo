from django.db import models


class Todo(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()

    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=255)

    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']
        verbose_name = 'Todo item'
        verbose_name_plural = 'Todo items'

    def __str__(self):
        return self.title
