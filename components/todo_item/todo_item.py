from django_components import component


@component.register("todo_item")
class TodoItem(component.Component):
    template_name = "todo_item/template.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    class Media:
        css = "todo_item/style.css"
        js = "todo_item/script.js"
