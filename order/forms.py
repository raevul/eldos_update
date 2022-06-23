from django.forms import ModelForm, ValidationError

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['email', 'phone', 'address', 'city', 'book']

    def clean_phone(self):
        data = self.cleaned_data
        phone = data.get('phone')
        if not phone.startswith('+996'):
            raise ValidationError('Number should start with "+996"')
        if len(phone) != 13:
            raise ValidationError('Invalid phone number')
        return phone
