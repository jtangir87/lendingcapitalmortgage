from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import PreApprovalForm, RefinanceForm

# Create your views here.


def pre_approval_page(request):
    if request.method == "POST":
        form = PreApprovalForm(request.POST or None)
        if form.is_valid():

            ### SEND EMAIL TO LCM ###
            template = get_template("emails/pre_approval_request.txt")
            context = {
                "first_name": form.cleaned_data.get('first_name'),
                "last_name": form.cleaned_data.get('last_name'),
                "email": form.cleaned_data.get('email'),
                "phone": form.cleaned_data.get('phone'),
                "credit_score": form.cleaned_data.get('credit_score'),
                "purchase_price": form.cleaned_data.get('purchase_price'),
                "down_payment": form.cleaned_data.get('down_payment'),
            }
            content = template.render(context)
            send_mail(
                "New Pre-Approval Request",
                content,
                "LCM WEBSITE <donotreply@philadelphiamedialab.com>",
                ["kstegena@outlook.com"],
                fail_silently=False,
            )

            return HttpResponseRedirect(reverse("thank_you"))

        else:
            errors = form.errors
            form = PreApprovalForm(request.POST)

            context = {
                "errors": errors,
                "form": form,
            }

    else:
        form = PreApprovalForm()
        context = {"form": form}

    return render(request, "pages/pre_approval_form.html", context)


def refinance_page(request):
    if request.method == "POST":
        form = RefinanceForm(request.POST or None)
        if form.is_valid():

            ### SEND EMAIL TO LCM ###
            template = get_template("emails/refinance_request.txt")
            context = {
                "first_name": form.cleaned_data.get('first_name'),
                "last_name": form.cleaned_data.get('last_name'),
                "email": form.cleaned_data.get('email'),
                "phone": form.cleaned_data.get('phone'),
                "credit_score": form.cleaned_data.get('credit_score'),
                "loan_balance": form.cleaned_data.get('loan_balance'),
                "address": form.cleaned_data.get('address'),
                "city": form.cleaned_data.get('city'),
                "state": form.cleaned_data.get('state'),
                "zip_code": form.cleaned_data.get('zip_code'),
            }
            content = template.render(context)
            send_mail(
                "New Refinance Request",
                content,
                "LCM WEBSITE <donotreply@philadelphiamedialab.com>",
                ["kstegena@outlook.com"],
                fail_silently=False,
            )

            return HttpResponseRedirect(reverse("thank_you"))

        else:
            errors = form.errors
            form = RefinanceForm(request.POST)

            context = {
                "errors": errors,
                "form": form,
            }

    else:
        form = RefinanceForm()
        context = {"form": form}

    return render(request, "pages/refinance_form.html", context)
