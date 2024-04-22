from django_components import component


@component.register("todo")
class Todo(component.Component):
    template_name = "todo/template.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    class Media:
        css = "todo/style.css"
        js = "todo/script.js"
