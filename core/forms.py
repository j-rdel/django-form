from django import forms
from django.core.mail.message import EmailMessage

from .models import Product

class ContactForm(forms.Form):
  name = forms.CharField(label='Name', max_length=100)
  email = forms.CharField(label='Email', max_length=100)
  about = forms.CharField(label='About', max_length=120)
  message = forms.CharField(label='Message', widget=forms.Textarea())

  def send_email(self):
    name = self.cleaned_data['name']
    email = self.cleaned_data['email']
    about = self.cleaned_data['about']
    message = self.cleaned_data['message']

    content = f'Name: {name}\nEmail: {email}\nAbout: {about}\nMessage: {message}'

    mail = EmailMessage(
      subject="Email sent by the django 2 system",
      body=content,
      from_email='contact@yourdomain.com',
      to=['contact@yourdomain.com'],
      headers={'Reply-To': email}
    )

    mail.send()

class ProductModelForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['name', 'price', 'inventory', 'image']