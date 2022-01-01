from django import forms

from snippets.models import Snippet, Comment


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'description')
