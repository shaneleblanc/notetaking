from django import forms
from notetaking.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']
