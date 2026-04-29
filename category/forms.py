from django import forms
from .models import TaskCategory


class TaskCategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = ['categoryName']
        widgets = {
            'categoryName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
        }
