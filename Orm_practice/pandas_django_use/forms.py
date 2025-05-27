from django import forms

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

BANK_CHOICES = [
    ('ICICI', 'ICICI NET BANK'),
    ('PNB', 'PUNJAB NATIONAL BANK'),
]

TRANSACTION_CHOICES = [
    ('SALE', 'Sale'),
    ('REFUND', 'Refund'),
]

class UploadForm(forms.Form):
    bank_name = forms.ChoiceField(choices=BANK_CHOICES, label='Bank Name')
    transaction_type = forms.ChoiceField(choices=TRANSACTION_CHOICES, label='Transaction Type')
    files = forms.FileField(
        widget=MultiFileInput(attrs={'multiple': True, 'name': 'files'}),
        label='Upload CSV Files'
    )
