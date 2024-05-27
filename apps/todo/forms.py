from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Submit, Layout
from django import forms
from django.forms import HiddenInput
from django.urls import reverse

from apps.todo.models import Todo, TodoItem


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('title', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("todo-create-view")
        self.helper.layout = Layout(
            Fieldset('Add todo', 'title', 'description'),
            Submit(name='add_todo_submit', value='Add todo'),
        )


class TodoItemForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = ('title', 'todo')
        widgets = {
            'todo': HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse("todo-create-view")
        self.helper.layout = Layout(
            Fieldset('Add todo', 'title', 'todo'),
            Submit(name='add_todo_submit', value='Add todo'),
        )
