from django.forms import ModelForm, fields
from app.models import TODO



class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title','status', 'priority']