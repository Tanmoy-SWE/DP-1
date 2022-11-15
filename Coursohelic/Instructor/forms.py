from django import forms
from django.forms import ClearableFileInput
from .models import PdfFiles
class PDFUpload(forms.ModelForm):
    class Meta:
        model = PdfFiles
        fields = ['name']
        widgets = {
            'name': ClearableFileInput(attrs={'multiple': True}),
        }