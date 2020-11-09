from django import forms


class PreApprovalForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    credit_score = forms.IntegerField(label="Estimated Credit Score")
    purchase_price = forms.IntegerField(label="Purchase Price", required=False)
    down_payment = forms.IntegerField(
        label="Down Payment Amount", required=False)


class RefinanceForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    credit_score = forms.IntegerField(label="Estimated Credit Score")
    loan_balance = forms.IntegerField(label="Loan Balance")
    address = forms.CharField(max_length=100, required=False, label="Street")
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=25, required=False)
    zip_code = forms.CharField(max_length=6, required=False)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)
