from django.forms import ModelForm
from budgetApp.models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = "date"

class RegisterForm(ModelForm):
    class Meta:
        model=users
        fields = ['name', 'address', 'mobilenum', 'emailid', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

class LoginForm(ModelForm):
    class Meta:
        model=users
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

    def clean(self):
        cleaned_data = super().clean()
        username=cleaned_data.get("username")
        if(users.objects.filter(username=username)):
            pass
        else:
            msg="no user exist in this name"
            self.add_error('username',msg)

class ExpenseForm(ModelForm):
    class Meta:
        model=expense
        fields=['category','expense_name','amount','date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].widget = DateInput()

    def clean(self):
        cleaned_data = super().clean()
        amount=cleaned_data.get("amount")

        if amount < 10:
            msg="please provide correct value for price"
            self.add_error("price",msg)

class ExpenseCategory(ModelForm):
    class Meta:
        model=category
        fields=['category_name']

class dateInsertForm(forms.Form):
        from_date=forms.DateField(widget=forms.SelectDateWidget)
        to_date = forms.DateField(widget=forms.SelectDateWidget)

class CategoryInsertForm(ModelForm):
    from_date = forms.DateField(widget=forms.SelectDateWidget)
    to_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=expense
        fields=['category']