from django_components import component


@component.register("form")
class Form(component.Component):
    template_name = "form/template.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(**kwargs)
        return context

    class Media:
        css = "form/style.css"
        js = "form/script.js"
