from django.forms import ModelForm
from .models import Program

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['p_name','department','total_credit', 'description']

