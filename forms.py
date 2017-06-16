from django import forms
import urllib


class SearchForm(forms.Form):
    tag = forms.CharField(label='Your tag',
                          max_length=100,
                          required=True)
    start_date = forms.DateTimeField(input_formats=['%Y-%m-%d'])
    end_date = forms.DateTimeField(input_formats=['%Y-%m-%d'])
    interval = forms.IntegerField()
    color = forms.CharField()
    def get_tag(self):
        return self.cleaned_data()

