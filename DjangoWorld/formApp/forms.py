from django import forms

class sampleForm(forms.Form):
    userName = forms.CharField(min_length=10,max_length=150,required=True,initial="tamilselvan",help_text="FirstName")
    password = forms.CharField(min_length=5,max_length=10, widget=forms.PasswordInput())
    email = forms.EmailField(min_length=150, widget=forms.EmailInput())
    age = forms.IntegerField()
    currency = forms.DecimalField(min_value=3, max_value=10, max_digits=3)
    isAdmin = forms.BooleanField()
    gender = forms.ChoiceField(choices=[("male","Male"),("female","Female"),("Trans","Transgender")],widget=forms.RadioSelect)
    day = forms.ChoiceField(choices=[("monday","Monday"),("tuesday","Tuesday"),("wednesday","Wednesday"),("thursday","Thursday"),("friday","Friday"),("saturday","Saturday")])
    date = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    day = forms.MultipleChoiceField(choices=[("monday","Monday"),("tuesday","Tuesday"),("wednesday","Wednesday"),("thursday","Thursday"),("friday","Friday"),("saturday","Saturday")])
    file = forms.FileField()
    image = forms.ImageField()
    description = forms.CharField(min_length=100,max_length=150, widget=forms.Textarea())
