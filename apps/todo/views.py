
from django.views.generic import ListView

from apps.todo.models import Todo


class IndexView(ListView):

    model = Todo
    template_name = "todo/index.html"
    context_object_name = "todos"
