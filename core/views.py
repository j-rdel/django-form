from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .forms import ContactForm, ProductModelForm
from .models import Product

def index(request):
  context = {
    'products': Product.objects.all()
  }

  return render(request, 'index.html', context)

def contact(request):
  form = ContactForm(request.POST or None)

  if str(request.method) == "POST":
    if form.is_valid():
      form.send_email()
      messages.success(request, "Email successfully sent!")
      form = ContactForm()
    else:
      messages.error(request, "Error sending email!")

  context = {
    'form': form
  }
  return render(request, 'contact.html', context)

def product(request):
  if str(request.user) == "jardelurban":
    if str(request.method) == 'POST':
      form = ProductModelForm(request.POST, request.FILES)
      if form.is_valid():
        form.save()

        messages.success(request, "Product successfully saved!")
        form = ProductModelForm()

      else:
        messages.error(request, "Error saving product!")
  
    else:
      form = ProductModelForm()
  
    context = {
      "form": form
    }

    return render(request, 'product.html', context)
  
  else:
    return redirect('index')
