from django_components import component


@component.register("modal")
class ModalBase(component.Component):
    template_name = "modal/base/template.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    class Media:
        css = "modal/style.css"
        js = "modal/script.js"
