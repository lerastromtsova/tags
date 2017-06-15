from django import forms
import urllib


class SearchForm(forms.Form):
    tag = forms.CharField(label='Your tag',
                          max_length=100,
                          required=True)

    def get_tag(self):
        return self.cleaned_data()

