from django_components import component


@component.register("modal_form")
class ModalForm(component.Component):
    template_name = "modal/form/template.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)

    class Media:
        css = "modal/form/style.css"
        js = "modal/form/script.js"
