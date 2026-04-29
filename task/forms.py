from django import forms
from .models import TaskModel
from category.models import TaskCategory


class TaskModelForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=TaskCategory.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-select',
            'size': '5',
        }),
        required=False,
        label="Categories",
        help_text="Hold Ctrl (or Cmd on Mac) to select multiple"
    )

    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription', 'is_completed']
        widgets = {
            'taskTitle': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title'
            }),
            'taskDescription': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter task description'
            }),
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if instance:
            self.fields['categories'].initial = instance.taskcategory_set.all()
