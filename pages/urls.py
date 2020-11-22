"""pages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.views.generic import TemplateView

from .views import newsletter_signup, pre_approval_page, refinance_page, ContactPage

urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    path('about', TemplateView.as_view(
        template_name='pages/about.html'), name="about"),
    path('services', TemplateView.as_view(
        template_name='pages/services.html'), name="services"),
    path('wall-of-fame', TemplateView.as_view(
        template_name='pages/wall_of_fame.html'), name="wall_of_fame"),
    path('contact', ContactPage.as_view(), name="contact"),
    path('mortgage-calculator', TemplateView.as_view(
        template_name='pages/mortgage_calc.html'), name="mortgage_calc"),
    path('thank-you', TemplateView.as_view(
        template_name='pages/thank_you.html'), name="thank_you"),
    path('privacy', TemplateView.as_view(
        template_name='pages/privacy_policy.html'), name="privacy_policy"),

    ## SERVICES ###
    path('services/fha-lending', TemplateView.as_view(
        template_name='pages/fha_lending.html'), name="fha"),
    path('services/conventional-lending', TemplateView.as_view(
        template_name='pages/conventional_lending.html'), name="conventional"),
    path('services/va-lending', TemplateView.as_view(
        template_name='pages/va_lending.html'), name="va"),
    path('services/non-qm-lending', TemplateView.as_view(
        template_name='pages/non_qm_lending.html'), name="non-qm"),
    path('services/jumbo-lending', TemplateView.as_view(
        template_name='pages/jumbo_lending.html'), name="jumbo"),
    path('services/refinancing', TemplateView.as_view(
        template_name='pages/refinancing.html'), name="refinancing"),
    path('services/dpa-lending', TemplateView.as_view(
        template_name='pages/dpa_lending.html'), name="dpa"),
    path('services/usda-lending', TemplateView.as_view(
        template_name='pages/usda_lending.html'), name="usda"),


    ## LOCAL LANDING ###
    path('bucks-county-mortgages', TemplateView.as_view(
        template_name='pages/bucks_county.html'), name="bucks_county"),
    path('montgomery-county-mortgages', TemplateView.as_view(
        template_name='pages/montgomery_county.html'), name="montgomery_county"),
    path('philadelphia-county-mortgages', TemplateView.as_view(
        template_name='pages/philadelphia_county.html'), name="philadelphia_county"),

    ## FORMS ##
    path("pre-approval", pre_approval_page, name="pre_approval_form"),
    path("refinance", refinance_page, name="refinance_form"),
    path("newsletter", newsletter_signup, name="newsletter_signup"),

]
