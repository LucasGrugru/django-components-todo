from django_components import component

from apps.todo.forms import TodoItemForm


@component.register("todo")
class Todo(component.Component):
    template_name = "todo/template.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['todo_item_form'] = TodoItemForm(initial={'todo': kwargs.get("todo")})
        return context

    class Media:
        css = "todo/style.css"
        js = "todo/script.js"
