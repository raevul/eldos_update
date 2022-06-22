from django import forms

PRODUCT_QUANTITY_CHOICES = [
    (i, str(i)) for i in range(1, 11)
]


class CartAddBookForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES)
    update = forms.BooleanField(required=False, widget=forms.HiddenInput)
