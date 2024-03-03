from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data['email']
        # Add custom validation logic for email, if desired (e.g., verifying existence in a database)
        return email
