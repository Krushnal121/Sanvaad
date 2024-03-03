from django.shortcuts import render
from .forms import ContactForm
from .models import ContactDetails

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process valid form data
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            #subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Create a new Contact object and save it to the database
            contact = ContactDetails(name=name, email=email, message=message)
            contact.save()

            # Success message or redirect to a confirmation page
            return render(request, 'contact.html', {'message': 'Your message has been sent!'})
    else:
        form = ContactForm()
        context = {'form': form}

    return render(request, 'contact.html', {'form': form})
