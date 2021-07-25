from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from .forms import PreApprovalForm, RefinanceForm, ContactForm

# Create your views here.


def home_cta(request):
    if request.method == "POST":
        ### SEND EMAIL TO LCM ###
        template = get_template("emails/pre_approval_request.txt")
        context = {
            "first_name": request.POST.get('name'),
            "email": request.POST.get('email'),
            "phone": request.POST.get('phone'),
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


def pre_approval_page(request):
    if request.method == "POST":
        form = PreApprovalForm(request.POST or None)
        if form.is_valid():
            honeypot = form.cleaned_data.get('address_hp')
            if not honeypot:
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
                return HttpResponseRedirect("https://myfakewebsite.com/")

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
            honeypot = form.cleaned_data.get('address_hp')
            if not honeypot:
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
                return HttpResponseRedirect("https://myfakewebsite.com/")

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


class ContactPage(FormView):
    form_class = ContactForm
    template_name = "pages/contact.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        honeypot = form.cleaned_data.get('address_hp')
        if not honeypot:
            template = get_template("emails/contact_us.txt")
            context = {
                "name": form.cleaned_data.get('name'),
                "email": form.cleaned_data.get('email'),
                "phone": form.cleaned_data.get('phone'),
                "message": form.cleaned_data.get('message'),
            }
            content = template.render(context)
            send_mail(
                "LCM CONTACT US",
                content,
                "LCM WEBSITE <donotreply@philadelphiamedialab.com>",
                ["kstegena@outlook.com"],
                fail_silently=False,
            )
            return super(ContactPage, self).form_valid(form)
        else:
            return HttpResponseRedirect("https://myfakewebsite.com/")


def newsletter_signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        template = get_template("emails/newsletter_signup.txt")

        content = template.render({"email": email})
        send_mail(
            "LCM NEWSLETTER SUBSCRIBE",
            content,
            "LCM WEBSITE <donotreply@philadelphiamedialab.com>",
            ["kstegena@outlook.com"],
            fail_silently=False,
        )
        return HttpResponseRedirect(reverse("thank_you"))
