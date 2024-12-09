from .models import Films
from django.forms import ModelForm, TextInput,Textarea

class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = '__all__'
        widgets = {
            'name': TextInput(),
            'description': TextInput(),
            'review': Textarea(attrs={'cols': 40, 'rows': 10}),
        }
