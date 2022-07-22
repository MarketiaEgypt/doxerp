from django.forms import ModelForm
from .models import Contact



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'company', 'phone', 'email', 'massege')
        # labels = {
        #     'name': _('Name'),
        # }
