from django.urls import reverse
from django.views.generic import ListView, CreateView

from apps.todo.models import Todo
from apps.todo.forms import TodoForm


class IndexView(ListView):

    model = Todo
    template_name = "todo/index.html"
    context_object_name = "todos"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["todo_form"] = TodoForm()
        return context


class TodoCreateView(CreateView):

    model = Todo
    form_class = TodoForm

    def get_success_url(self):
        return reverse("index")
