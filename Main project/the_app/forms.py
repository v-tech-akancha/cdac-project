from django import forms

class File_saving_form(forms.Form):
    myfile = forms.FileField()

class ContactForm(forms.Form):
    name= forms.CharField(max_length=500, label="Name")
    email= forms.EmailField(max_length=2000, label="",widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email here'}))
    comment= forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'Enter your comment here'}))
    