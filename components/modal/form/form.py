from django_components import component


@component.register("modal_form")
class ModalForm(component.Component):
    template_name = "modal/form/template.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(**kwargs)
        return context

    class Media:
        css = "modal/form/style.css"
        js = "modal/form/script.js"
