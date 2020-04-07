from django import forms

class JurosForm(forms.Form):
    montante = forms.FloatField()
    capital = forms.FloatField()
    taxa_de_juros = forms.FloatField()
    tempo = forms.IntegerField()